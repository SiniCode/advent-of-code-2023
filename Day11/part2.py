import numpy as np
from itertools import combinations


class GalaxyPaths:
    def __init__(self, filename='Day11/input.txt'):
        self.universe = self.get_universe(filename)
        self.galaxy_coords = self.get_galaxy_coords()
        self.expanded_row_idx = self.find_rows_to_expand(self.universe)
        self.expanded_col_idx = self.find_cols_to_expand(self.universe)

    def get_universe(self, filename):
        with open(filename) as file:
            lines = file.readlines()
            lines = [list(line.strip()) for line in lines]

        universe = np.array(lines)
        return universe

    def get_galaxy_coords(self):
        coords = np.where(self.universe=='#')

        return list(zip(*coords))

    def find_rows_to_expand(self, universe):
        row_idx = []
        for i, row in enumerate(universe):
            if not '#' in row:
                row_idx.append(i)

        return row_idx
    
    def find_cols_to_expand(self, universe):
        return self.find_rows_to_expand(universe.T)
    
    def calculate_shortest_path(self, coords1, coords2):
        smaller_x = min(coords1[0], coords2[0])
        bigger_x = max(coords1[0], coords2[0])
        smaller_y = min(coords1[1], coords2[1])
        bigger_y = max(coords1[1], coords2[1])

        x_distance = bigger_x - smaller_x
        for i in self.expanded_row_idx:
            if i in range(smaller_x, bigger_x):
                x_distance += 999999

        y_distance = bigger_y - smaller_y
        for i in self.expanded_col_idx:
            if i in range(smaller_y, bigger_y):
                y_distance += 999999

        return x_distance + y_distance
    
    def calculate_sum_of_shortest_paths(self):
        galaxy_pairs = combinations(self.galaxy_coords, 2)
        result = 0

        for galaxies in galaxy_pairs:
            result += self.calculate_shortest_path(galaxies[0], galaxies[1])

        return result


    
if __name__ == '__main__':
    GP = GalaxyPaths()
    print(GP.calculate_sum_of_shortest_paths())  # correct: 569052586852