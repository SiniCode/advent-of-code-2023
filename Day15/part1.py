

class InitializationCalculator:
    def __init__(self, filename='Day15/input.txt'):
        self.init_sequence = self.get_init_sequence(filename)

    def get_init_sequence(self, filename):
        with open(filename) as file:
            init_sequence = file.readline().strip().split(',')

        return init_sequence
    
    def calculate_hash(self, step):
        current = 0
        for char in step:
            code = ord(char)
            current += code
            current *= 17
            current = current % 256

        return current
    
    def calculate_sum_of_hashes(self):
        result = 0
        for step in self.init_sequence:
            result += self.calculate_hash(step)

        return result

if __name__ == '__main__':
    IC = InitializationCalculator()
    print(IC.calculate_sum_of_hashes())  # correct: 511257