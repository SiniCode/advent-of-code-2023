import re


def get_total_points(filename='Day4/input.txt'):
    total_points = 0

    with open(filename) as file:
        for line in file.readlines():
            numbers = line.split(':')[1].split('|')
            winning_numbers = re.findall(r'\d+', numbers[0])
            matching_count = 0
            for number in re.findall(r'\d+', numbers[1]):
                if number in winning_numbers:
                    matching_count += 1
            
            if matching_count > 0:
                total_points += 2 ** (matching_count-1)

    return total_points
      

if __name__ == '__main__':
    print(get_total_points())  # correct: 24160