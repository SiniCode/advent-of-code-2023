import re


class MapReader:
    def __init__(self, filename='Day8/input.txt'):
        self.instructions, self.nodes = self.read_input(filename)

    def read_input(self, filename):
        nodes = {}

        with open(filename) as file:
            lines = file.readlines()

        instructions = lines[0].strip().replace('L', '0').replace('R', '1')
        for line in lines[2:]:
            parts = line.split(' = ')
            nodes[parts[0]] = re.findall(r'[A-Z]{3}', parts[1])

        return instructions, nodes
    
    def count_steps(self):
        steps = 0
        i = 0
        current = 'AAA'
        instruction_length = len(self.instructions)

        while current != 'ZZZ':
            steps += 1
            current = self.nodes[current][int(self.instructions[i])]
            if i < instruction_length - 1:
                i += 1
            else:
                i = 0

        return steps
    

if __name__ == '__main__':
    MR = MapReader()
    print(MR.count_steps())  # correct: 12599