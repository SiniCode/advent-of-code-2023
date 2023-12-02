def get_numbers():
    
    numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
               'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
               '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

    return numbers

def get_first_number_in_line(numbers, line):

    i = 0
    while i < len(line):
        section = line[i:]
        for num in numbers.keys():
            if section.startswith(num):
                return numbers[num]
        i += 1

    return ''

def get_last_number_in_line(numbers, line):

    i = len(line)
    while i > 0:
        section = line[:i]
        for num in numbers.keys():
            if section.endswith(num):
                return numbers[num]
        i -= 1

    return ''

def get_sum_of_calibration_values(filename='input.txt'):
    numbers = get_numbers()
    calibration_sum = 0

    with open(filename) as file:
        for line in file.readlines():
            calibration_value = get_first_number_in_line(numbers, line)
            calibration_value += get_last_number_in_line(numbers, line)
            calibration_sum += int(calibration_value)

    return calibration_sum


if __name__ == '__main__':
    print(get_sum_of_calibration_values())  # correct: 55093
