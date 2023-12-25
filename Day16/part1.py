import numpy as np

class Contraption:
    def __init__(self, filename='Day16/input.txt'):
        self.next = [(0,0,'r')]
        self.visited = set([(0,0,'r')])
        self.contraption = self.get_contraption(filename)
        self.energized = np.zeros(self.contraption.shape, dtype=int)

    def get_contraption(self, filename):
        with open(filename) as file:
            contraption = file.readlines()
            contraption = [list(line.strip()) for line in contraption]

        return np.array(contraption)
    
    def get_next_coords(self, current):
        char = self.contraption[current[0]][current[1]]
        i = current[0]
        j = current[1]
        direction = current[2]
        n, m = self.contraption.shape
        next_coords = []

        if char == '.':
            if direction == 'r' and j+1 < m:
                return [(i, j+1, direction)]
            if direction == 'd' and i+1 < n:
                return [(i+1, j, direction)]
            if direction == 'l' and j > 0:
                return [(i, j-1, direction)]
            if direction == 'u' and i > 0:
                return [(i-1, j, direction)]
        
        if char == '/':
            if direction == 'r' and i > 0:
                return [(i-1, j, 'u')]
            if direction == 'd' and j > 0:
                return [(i, j-1, 'l')]
            if direction == 'l' and i+1 < n:
                return [(i+1, j, 'd')]
            if direction == 'u' and j+1 < m:
                return [(i, j+1, 'r')]
        
        if char == '\\':
            if direction == 'r' and i+1 < n:
                return [(i+1, j, 'd')]
            if direction == 'd' and j+1 < m:
                return [(i, j+1, 'r')]
            if direction == 'l' and i > 0:
                return [(i-1, j, 'u')]
            if direction == 'u' and j > 0:
                return [(i, j-1, 'l')]
        
        if char == '-':
            if direction == 'r' and j+1 < m:
                return [(i, j+1, direction)]
            if direction == 'l' and j > 0:
                return [(i, j-1, direction)]
            if j > 0:
                next_coords.append((i, j-1, 'l'))
            if j+1 < m:
                next_coords.append((i, j+1, 'r'))
        
        if char == '|':
            if direction == 'u' and i > 0:
                return [(i-1, j, direction)]
            if direction == 'd' and i+1 < n:
                return [(i+1, j, direction)]
            if i > 0:
                next_coords.append((i-1, j, 'u'))
            if i+1 < n:
                next_coords.append((i+1, j, 'd'))
        
        return next_coords
    
    def move(self):
        new_list = self.next.copy()
        for coords in self.next:
            self.energized[coords[0]][coords[1]] = 1
            next_coords = self.get_next_coords(coords)
            for n_coords in next_coords:
                if n_coords not in self.visited:
                    new_list.append(n_coords)
            self.visited.update(next_coords)
            new_list.remove(coords)
        self.next = new_list

    def calculate_energized_tiles(self):
        while len(self.next) > 0:
            self.move()

        return self.energized.sum()
            

if __name__ == '__main__':
    C = Contraption()
    print(C.calculate_energized_tiles())  # correct: 7870
