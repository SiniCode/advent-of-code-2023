class BoatRacer:
    def __init__(self, record='Day6/input.txt'):
        self.record = self.read_record(record)

    def read_record(self, record_file):
        with open(record_file) as file:
            lines = file.readlines()

        time = lines[0].strip().replace(' ', '').split(':')[1]
        distance = lines[1].strip().replace(' ', '').split(':')[1]
        
        return (int(time), int(distance))
    
    def possible_distances(self, time):
        distances = []
        
        for charge_time in range(time):
            distances.append(charge_time * (time - charge_time))

        return distances
    
    def count_winning_distances(self):
        possible_distances = self.possible_distances(self.record[0])
        winning_distances = [dist for dist in possible_distances if dist > self.record[1]]

        return len(winning_distances)
    

if __name__ == '__main__':
    BR = BoatRacer()
    print(BR.count_winning_distances())  # correct: 42250895