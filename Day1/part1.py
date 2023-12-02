def get_sum_of_calibration_values(filename='Day1/input.txt'):
    numbers = '0123456789'
    calibration_sum = 0

    with open(filename) as file:
        for line in file.readlines():
            calibration_value = ''
            for char in line:
                if char in numbers:
                    calibration_value += char
                    break
            for char in line[::-1]:
                if char in numbers:
                    calibration_value += char
                    break

            calibration_sum += int(calibration_value)

    return calibration_sum


if __name__ == '__main__':
    print(get_sum_of_calibration_values())  # correct: 55002