import re


class BoatRacer:
    def __init__(self, records='Day6/input.txt'):
        self.records = self.read_records(records)

    def read_records(self, record_file):
        with open(record_file) as file:
            lines = file.readlines()

        time = re.findall(r'\d+', lines[0])
        distance = re.findall(r'\d+', lines[1])

        records = []
        for i, value in enumerate(time):
            records.append((int(value), int(distance[i])))
        
        return records
    
    def possible_distances(self, time):
        distances = []
        
        for charge_time in range(time):
            distances.append(charge_time * (time - charge_time))

        return distances
    
    def count_winning_distances(self, record):
        possible_distances = self.possible_distances(record[0])
        winning_distances = [dist for dist in possible_distances if dist > record[1]]

        return len(winning_distances)
    
    def multiply_counts(self):
        counts = 1
        for record in self.records:
            counts *= self.count_winning_distances(record)

        return counts

if __name__ == '__main__':
    BR = BoatRacer()
    print(BR.multiply_counts())  # correct: 449820