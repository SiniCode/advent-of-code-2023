import numpy as np

class Hike:
    def __init__(self, filename='Day23/input.txt'):
        self.landscape = self.read_landscape(filename)

    def read_landscape(self, filename):
        with open(filename) as file:
            lines = file.readlines()
            landscape = [list(line.strip()) for line in lines]
        
        return np.array(landscape)
    
    def take_step(self, x, y, previous):
        if x == self.landscape.shape[0]-1:
            return []
        
        next_coords = []
        current = self.landscape[x][y]

        if current == '>':
            next_coords.append((x, y+1))
        elif current == '<':
            next_coords.append((x, y-1))
        elif current == 'v':
            next_coords.append((x+1, y))
        elif current == '^':
            next_coords.append((x-1, y))
        else:
            if (x > 0) and (self.landscape[x-1][y] in '.^') and ((x-1, y) != previous):
                next_coords.append((x-1, y))
            if (x < self.landscape.shape[0]-1) and (self.landscape[x+1][y] in '.v') and ((x+1, y) != previous):
                next_coords.append((x+1, y))
            if (y > 0) and (self.landscape[x][y-1] in '.<') and ((x, y-1) != previous):
                next_coords.append((x, y-1))
            if (y < self.landscape.shape[1]-1) and (self.landscape[x][y+1] in '.>') and ((x, y+1) != previous):
                next_coords.append((x, y+1))

        return list(zip(next_coords, [(x,y)]*len(next_coords)))

    def find_longest_hike_length(self):
        next_coords = self.take_step(0, 1, (0, 0))
        steps = 0
        while next_coords != []:
            new_coords = []
            for coords in next_coords:
                new_coords += self.take_step(coords[0][0], coords[0][1], coords[1])

            steps += 1
            next_coords = new_coords
    
        return steps
    
if __name__ == '__main__':
    H = Hike()
    print(H.find_longest_hike_length())  # correct: 2330
 