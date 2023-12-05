import re

class AlmanacInterpreter:
    def __init__(self, input_file='Day5/input.txt'):
        with open(input_file) as file:
            input_list = file.readlines()
        
        self.seeds = self.get_seeds(input_list[0])
        self.map_names = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
                          'water-to-light', 'light-to-temperature', 'temperature-to-humidity',
                          'humidity-to-location']
        self.mappings = self.get_mappings(input_list)

    def get_seeds(self, seed_line):
        seeds = re.findall(r'\d+', seed_line)
        seeds = [int(seed) for seed in seeds]
        return seeds
    
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
    
    def find_corresponding_value(self, value1, mapping):
        for m in mapping:
            if value1 in range(m[1], m[1]+m[2]):
                dist = value1 - m[1]
                return m[0] + dist
            
        return value1
    
    def map_seed_to_location(self, seed):
        for name in self.map_names:
            seed = self.find_corresponding_value(seed, self.mappings[name])

        return seed
    
    def find_seed_locations(self):
        locations = [self.map_seed_to_location(seed) for seed in self.seeds]
        return locations
    
    def find_lowest_location(self):
        locations = self.find_seed_locations()
        return min(locations)

    
    
if __name__ == '__main__':
    AI = AlmanacInterpreter()
    print(AI.find_lowest_location())  # correct: 389056265