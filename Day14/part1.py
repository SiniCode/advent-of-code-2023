import numpy as np


class RockPlatform:
    def __init__(self, filename='Day14/input.txt'):
        self.platform = self.get_platform(filename)

    def get_platform(self, filename):
        platform = []

        with open(filename) as file:
            for line in file:
                platform.append(list(line.strip()))

        return np.array(platform)
    
    def tilt_to_north(self, arr):
        cube_idx = [i for i, c in enumerate(arr) if c == '#']

        if not cube_idx:
            return np.array(sorted(arr, reverse=True))
        
        tilted = []
        i = 0
        for j in cube_idx:
            part = arr[i:j]
            tilted += sorted(part, reverse=True)
            tilted += ['#']
            i = j+1
        if i < len(arr):
            part = arr[i:]
            tilted += sorted(part, reverse=True)
    
        return np.array(tilted)
    
    def tilt_platform(self):
        tilted_platform = self.platform.T
        n_rows = tilted_platform.shape[0]
        
        for i in range(n_rows):
            tilted_platform[i] = self.tilt_to_north(tilted_platform[i])

        return tilted_platform
    
    def calculate_total_load(self):
        tilted_platform = self.tilt_platform()
        total = 0

        for arr in tilted_platform:
            total += sum([len(arr)-i for i, c in enumerate(arr) if c == 'O'])

        return total

if __name__ == '__main__':
    RP = RockPlatform()
    print(RP.calculate_total_load())  # correct: 110128