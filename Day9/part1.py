import re


class ReportReader:
    def __init__(self, filename='Day9/input.txt'):
        self.histories = self.get_histories(filename)

    def get_histories(self, filename):
        with open(filename) as file:
            lines = file.readlines()

        histories = [re.findall(r'-?\d+', line) for line in lines]
        histories = [list(map(int, history)) for history in histories]

        return histories
    
    def get_processing_steps(self, history, steps):
        if not any(history):
            return steps
        
        previous_step = []
        for i in range(len(history) - 1):
            previous_step.append(history[i+1]-history[i])
        
        steps.append(previous_step)
        return self.get_processing_steps(previous_step, steps)
    
    def find_next_value(self, history):
        processing_steps = [history] + self.get_processing_steps(history, [])
        processing_steps.reverse()

        sums = [0]
        for step in processing_steps[1:]:
            sums.append(step[-1] + sums[-1])

        return sums[-1]
    
    def calculate_sum_of_next_values(self):
        next_values = [self.find_next_value(history) for history in self.histories]
        return sum(next_values)
    
if __name__ == '__main__':
    RR = ReportReader()
    print(RR.calculate_sum_of_next_values())  # correct: 1581679977