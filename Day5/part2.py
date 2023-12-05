import re
from math import inf

class AlmanacInterpreter:
    def __init__(self, input_file='Day5/input.txt'):
        with open(input_file) as file:
            input_list = file.readlines()
        
        self.seed_ranges = self.get_seeds(input_list[0])

        self.map_names = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
                          'water-to-light', 'light-to-temperature', 'temperature-to-humidity',
                          'humidity-to-location']
        self.mappings = self.get_mappings(input_list)

    def get_seeds(self, seed_line):
        seed_values = re.findall(r'\d+', seed_line)
        seed_values = [int(num) for num in seed_values]

        return seed_values
    
    def get_mapping(self, input_list, title):
        mapping = []
        start = input_list.index(f'{title} map:\n')
        for line in input_list[start+1:]:
            if line == '\n':
                break
            numbers = re.findall(r'\d+', line)
            mapping.append([int(num) for num in numbers])
        
        return mapping
    
    def get_mappings(self, input_list):
        mappings = {}
        
        for name in self.map_names:
            mappings[name] = self.get_mapping(input_list, name)

        return mappings
    
    def find_corresponding_value(self, value2, mapping):
        for m in mapping:
            if value2 in range(m[0], m[0]+m[2]):
                dist = value2 - m[0]
                return m[1] + dist
            
        return value2
    
    def map_location_to_seed(self, seed):
        for name in reversed(self.map_names):
            seed = self.find_corresponding_value(seed, self.mappings[name])

        return seed
    
    def get_sorted_location_ranges(self):
        loc_data = self.mappings['humidity-to-location']
        loc_ranges = []
        for data in loc_data:
            loc_ranges.append((data[0], data[0]+data[2]))
        
        return sorted(loc_ranges)
    
    def is_in_seeds(self, seed):
        for i, value in enumerate(self.seed_ranges):
            if i % 2 == 0:
                if seed in range(value, value+self.seed_ranges[i+1]):
                    return True
        return False

    def find_lowest_location(self):
        loc_ranges = self.get_sorted_location_ranges()
        first = loc_ranges[0][0]
        if first != 0:
            loc_ranges = [(0, first)] + loc_ranges

        for start, end in loc_ranges:
            print(start)
            for loc in range(start, end):
                seed = self.map_location_to_seed(loc)
                if self.is_in_seeds(seed):
                    return loc
                
        return -1

    
    
if __name__ == '__main__':
    AI = AlmanacInterpreter()
    print(AI.find_lowest_location())  # correct: 137516820