def game_is_possible(gameline):
    cubes_in_play = {'red': 12, 'green': 13, 'blue': 14}

    cube_sets = gameline.split(': ')[1]
    for cube_set in cube_sets.split('; '):
        for cubes in cube_set.split(', '):
            number, color = tuple(cubes.split(' '))
            if cubes_in_play[color] < int(number):
                return False
    return True

def get_sum_of_possible_ids(filename='Day2/input.txt'):
    sum_of_ids = 0

    with open(filename) as file:
        for line in file.readlines():
            if game_is_possible(line.strip()):
                sum_of_ids += int(line.split(':')[0].split(' ')[1])

    return sum_of_ids


if __name__ == '__main__':
    print(get_sum_of_possible_ids())  # correct: 2416