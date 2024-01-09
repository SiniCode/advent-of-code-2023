import numpy as np

class Garden:
    def __init__(self, filename='Day21/input.txt'):
        self.map = self.read_map_file(filename)

    def read_map_file(self, filename):
        with open(filename) as file:
            lines = file.readlines()
            garden_map = [list(line.strip()) for line in lines]

        return np.array(garden_map)
    
    def find_start(self):
        start = np.where(self.map == 'S')
        return start[0][0], start[1][0]

    def take_step(self, coords):
        next_coords = []

        for coord in coords:
            x = coord[0]
            y = coord[1]
            if x > 0 and self.map[x-1][y] != '#':
                next_coords.append((x-1, y))
            if x < self.map.shape[0]-1 and self.map[x+1][y] != '#':
                next_coords.append((x+1, y))
            if y > 0 and self.map[x][y-1] != '#':
                next_coords.append((x, y-1))
            if y < self.map.shape[1]-1 and self.map[x][y+1] != '#':
                next_coords.append((x, y+1))

        return list(set(next_coords))

    def count_garden_plots(self, steps=64):
        x, y = self.find_start()
        coords = [(x, y)]

        for _ in range(steps):
            coords = self.take_step(coords)

        return len(coords)
    
if __name__ == '__main__':
    G = Garden()
    print(G.count_garden_plots(steps=64))  # correct: 3809
