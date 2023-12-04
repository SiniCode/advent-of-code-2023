import re


def get_generated_cards(filename):
    generated_cards = {}

    with open(filename) as file:
        for i, line in enumerate(file.readlines()):
            numbers = line.split(':')[1].split('|')
            winning_numbers = re.findall(r'\d+', numbers[0])
            matching_count = 0
            for number in re.findall(r'\d+', numbers[1]):
                if number in winning_numbers:
                    matching_count += 1
            
            generated_cards[i] = list(range(i+1, i+matching_count+1))

    return generated_cards

def get_copies(card, generated_cards):
    copies = generated_cards[card]
    result = copies.copy()
    for copy in copies:
        result += get_copies(copy, generated_cards)
    return result

def get_total_cards(filename='Day4/input.txt'):
    generated_cards = get_generated_cards(filename)
    all_cards = list(generated_cards.keys())

    for card in generated_cards.keys():
        all_cards += get_copies(card, generated_cards)

    return len(all_cards)


if __name__ == '__main__':
    print(get_total_cards())  # correct: 5659035