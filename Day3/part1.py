def is_symbol(char):
    return char not in '0123456789.'

def is_number(char):
    return char in '0123456789'

def extract_number(lines, i, j):
    line = lines[i]
    number = line[j]
    lines[i][j] = '.'

    k = j-1
    while k >= 0 and is_number(line[k]):
        number = line[k] + number
        lines[i][k] = '.'
        k -= 1
    
    k = j+1
    while k < len(line) and is_number(line[k]):
        number += line[k]
        lines[i][k] = '.'
        k += 1

    return int(number)

def get_adjacent_numbers(lines, i, j):
    numbers = []

    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x < 0 or x >= len(lines):
                continue
            if y < 0 or y >= len(lines[0]):
                continue
            
            if is_number(lines[x][y]):
                numbers.append(extract_number(lines, x, y))

    return numbers

def get_sum_of_part_numbers(filename='Day3/input.txt'):
    result = 0

    with open(filename) as file:
        lines = file.readlines()
        lines = [list(line.strip()) for line in lines]

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if is_symbol(lines[i][j]):
                result += sum(get_adjacent_numbers(lines, i, j))

    return result


if __name__ == '__main__':
    print(get_sum_of_part_numbers())
