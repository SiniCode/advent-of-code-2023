import numpy as np


class PipeLoop:
    def __init__(self, filename='Day10/input.txt'):
        self.pipes = self.get_pipes(filename)
        self.shape = self.pipes.shape
        self.start_idx = self.get_start_index()
        self.visited = []

    def get_pipes(self, filename):
        pipes = []
        with open(filename) as file:
            for line in file:
                line = line.strip()
                pipes.append(list(line))

        return np.array(pipes)
    
    def get_start_index(self):
        i = np.where(self.pipes == 'S')
        return (i[0][0], i[1][0])
    
    def next_pipe(self, i, j, pipe):
        if pipe in ['S', '|', 'L', 'J'] and i > 0 and (i-1, j) not in self.visited:
            pipe_above = self.pipes[i-1][j]
            if pipe_above in ['|', '7', 'F', 'S']:
                self.visited.append((i-1, j))
                return (i-1, j, pipe_above)
            
        if pipe in ['S', 'L', 'F', '-'] and j < self.shape[1]-1 and (i, j+1) not in self.visited:
            pipe_right = self.pipes[i][j+1]
            if pipe_right in ['7', 'J', '-', 'S']:
                self.visited.append((i, j+1))
                return (i, j+1, pipe_right)
            
        if pipe in ['S', '|', '7', 'F'] and i < self.shape[0]-1 and (i+1, j) not in self.visited:
            pipe_below = self.pipes[i+1][j]
            if pipe_below in ['|', 'J', 'L', 'S']:
                self.visited.append((i+1, j))
                return (i+1, j, pipe_below)
            
        if pipe in ['S', '7', 'J', '-'] and j > 0 and (i, j-1) not in self.visited:
            pipe_left = self.pipes[i][j-1]
            if pipe_left in ['F', 'L', '-', 'S']:
                self.visited.append((i, j-1))
                return (i, j-1, pipe_left)
            
        return (self.start_idx[0], self.start_idx[1], 'S')

    def get_steps_to_farthest_point(self):
        self.visited = [self.start_idx]
        next_pipe = self.next_pipe(self.start_idx[0], self.start_idx[1], 'S')
        while next_pipe[2] != 'S':
            next_pipe = self.next_pipe(next_pipe[0], next_pipe[1], next_pipe[2])

        return len(self.visited) // 2

    

if __name__ == '__main__':
    PL = PipeLoop()
    print(PL.get_steps_to_farthest_point())  # correct: 6942