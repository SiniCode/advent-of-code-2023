def greater_than(a,b):
    return a > b

def less_than(a,b):
    return a < b

def always_true(a, b):
    return True


class PartSorter:
    def __init__(self, filename='Day19/input.txt'):
        self.workflows, self.parts = self.read_input_file(filename)
        self.accepted = []
        self.rejected = []

    def read_input_file(self, filename):
        workflows = dict()
        part_list = []
        change = False
        with open(filename) as file:
            for line in file:
                if line == '\n':
                    change = True
                elif not change:
                    workflow, rules = line.split('{')
                    rules = rules.strip('}\n')
                    rules = rules.split(',')
                    processed_rules = []
                    for rule in rules[:-1]:
                        parts = rule.split(':')
                        if '<' in parts[0]:
                            func = less_than
                            rule_parts = parts[0].split('<')
                        else:
                            func = greater_than
                            rule_parts = parts[0].split('>')
                        processed_rules.append((rule_parts[0], int(rule_parts[1]), func, parts[1]))
                    processed_rules.append(('x', 0, always_true, rules[-1]))
                    workflows[workflow] = processed_rules
                else:
                    parts = line.strip('{}\n').split(',')
                    ratings = {}
                    for part in parts:
                        pparts = part.split('=')
                        ratings[pparts[0]] = int(pparts[1])
                    part_list.append(ratings)

        return workflows, part_list
    
    def apply_rules(self, part, rules):
        for rule in rules:
            func = rule[2]
            if func(part[rule[0]], rule[1]):
                if rule[3] == 'A':
                    if not part in self.accepted:
                        self.accepted.append(part)
                    return
                elif rule[3] == 'R':
                    if not part in self.rejected:
                        self.rejected.append(part)
                    return
                else:
                    self.apply_rules(part, self.workflows[rule[3]])
                    return
    
    def process_parts(self):
        for part in self.parts:
            self.apply_rules(part, self.workflows['in'])

    def calculate_sum_of_accepted(self):
        self.process_parts()
        result = 0
        for part in self.accepted:
            result += sum(part.values())
        return result

    
if __name__ == '__main__':
    PS = PartSorter()
    print(PS.calculate_sum_of_accepted())  # correct: 421983

            