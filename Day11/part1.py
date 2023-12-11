import numpy as np
from itertools import combinations


class GalaxyPaths:
    def __init__(self, filename='Day11/input.txt'):
        self.galaxy_coords = self.get_galaxy_coords(filename)

    def get_galaxy_coords(self, filename):
        with open(filename) as file:
            lines = file.readlines()
            lines = [list(line.strip()) for line in lines]

        universe = np.array(lines)
        expanded_uni = self.expand_universe(universe, False)

        coords = np.where(expanded_uni=='#')

        return list(zip(*coords))

    def expand_universe(self, universe, once):
        expanded = []
        for row in universe:
            expanded.append(row)
            if not '#' in row:
                expanded.append(row)

        expanded = np.array(expanded)
        expanded = expanded.T

        if once:
            return expanded
        return self.expand_universe(expanded, True)
    
    def calculate_shortest_path(self, coords1, coords2):
        return abs(coords2[0] - coords1[0]) + abs(coords2[1] - coords1[1])
    
    def calculate_sum_of_shortest_paths(self):
        galaxy_pairs = combinations(self.galaxy_coords, 2)
        result = 0

        for galaxies in galaxy_pairs:
            result += self.calculate_shortest_path(galaxies[0], galaxies[1])

        return result


    
if __name__ == '__main__':
    GP = GalaxyPaths()
    print(GP.calculate_sum_of_shortest_paths())  # correct: 9724940
