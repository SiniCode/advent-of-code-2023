def get_cubes_in_play(gameline):
    cubes_in_play = {'red': 0, 'green': 0, 'blue': 0}

    cube_sets = gameline.split(': ')[1]
    for cube_set in cube_sets.split('; '):
        for cubes in cube_set.split(', '):
            number, color = tuple(cubes.split(' '))
            if cubes_in_play[color] < int(number):
                cubes_in_play[color] = int(number)
            
    return cubes_in_play

def get_sum_of_powers(filename='Day2/input.txt'):
    sum_of_powers = 0

    with open(filename) as file:
        for line in file.readlines():
            cubes = get_cubes_in_play(line.strip())
            power = cubes['red'] * cubes['green'] * cubes['blue']
            sum_of_powers += power

    return sum_of_powers


if __name__ == '__main__':
    print(get_sum_of_powers())  # correct: 63307