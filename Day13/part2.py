import numpy as np


class ReflectionDetector:
    def __init__(self, filename='Day13/input.txt'):
        self.patterns = self.get_patterns(filename)

    def get_patterns(self, filename):
        patterns = []
        with open(filename) as file:
            pattern = []
            for line in file:
                if line == '\n':
                    patterns.append(np.array(pattern))
                    pattern = []
                else:
                    pattern.append(list(line.strip()))
        
        patterns.append(np.array(pattern))
        return patterns
    
    def find_vertical_reflection_line(self, pattern):
        n_col = pattern.shape[1]

        for i in range(1, n_col):
            width = min(i, n_col-i)
            left = pattern[:, i-width:i]
            right = pattern[:, i:i+width]
            match = np.fliplr(left) == right
            if match.sum() == match.size - 1:
                return i
            
        return -1
    
    def find_horizontal_reflection_line(self, pattern):
        return self.find_vertical_reflection_line(pattern.T)
    
    def calculate_note_summary(self):
        verticals = 0
        horizontals = 0

        for pattern in self.patterns:
            note = self.find_vertical_reflection_line(pattern)
            if note == -1:
                horizontals += self.find_horizontal_reflection_line(pattern)
            else:
                verticals += note

        return 100 * horizontals + verticals

            
if __name__ == '__main__':
    RD = ReflectionDetector()
    print(RD.calculate_note_summary())