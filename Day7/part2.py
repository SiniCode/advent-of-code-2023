class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.hand_types = ['five of a kind', 'four of a kind', 'full house',
                           'three of a kind', 'two pair', 'one pair', 'high card']
        self.checks = [self.is_five_of_kind, self.is_four_of_kind, self.is_full_house,
                       self.is_three_of_kind, self.is_two_pair, self.is_one_pair, self.is_high_card]
        self.card_points = self.get_card_points()
        
    def get_card_points(self):
        points = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 1,
            'T': 10
        }
        for n in '98765432':
            points[n] = int(n)

        return points

    def __gt__(self, other):
        for i, c in enumerate(self.cards):
            if c != other.cards[i]:
                return self.card_points[c] > self.card_points[other.cards[i]]
        return False
    
    def __eq__(self, other):
        return self.cards == other.cards
    
    def __lt__(self, other):
        for i, c in enumerate(self.cards):
            if c != other.cards[i]:
                return self.card_points[c] < self.card_points[other.cards[i]]
        return False
    
    def get_counts(self):
        counts = {'J': 0}
        for c in set(self.cards):
            counts[c] = self.cards.count(c)
        return counts

    def is_five_of_kind(self):
        unique = set(self.cards)
        unique.discard('J')
        return len(unique) in [0,1]
        
    def is_four_of_kind(self):
        counts = self.get_counts()
        for card, count in counts.items():
            if card != 'J' and count + counts['J'] == 4:
                return True
            
        return False

    def is_full_house(self):
        counts = self.get_counts()
        if counts['J'] == 0 and 2 in counts.values() and 3 in counts.values():
            return True
        if counts['J'] == 1 and list(counts.values()).count(2) == 2:
            return True
        
        return False

    def is_three_of_kind(self):
        if self.is_five_of_kind() or self.is_four_of_kind() or self.is_full_house():
            return False
        
        counts = self.get_counts()
        if counts['J'] == 0 and 3 in counts.values():
            return True
        if counts['J'] == 1 and 2 in counts.values():
            return True
        if counts['J'] == 2:
            return True
        
        return False

    def is_two_pair(self):
        unique = set(self.cards)
        unique.discard('J')
        return len(unique) == 3 and not self.is_three_of_kind()
    
    def is_one_pair(self):
        unique = set(self.cards)
        unique.discard('J')
        return len(unique) == 4
    
    def is_high_card(self):
        unique = set(self.cards)
        unique.discard('J')
        return len(unique) == 5

    def is_hand_type(self, h_type):
        i = self.hand_types.index(h_type)
        check = self.checks[i]

        return check()

class CamelCards:
    def __init__(self, card_file='Day7/input.txt'):
        self.hands = self.read_card_file(card_file)
        
    def read_card_file(self, filename):
        hands = []
        with open(filename) as file:
            for line in file:
                parts = line.split()
                hands.append(Hand(parts[0], int(parts[1])))

        return hands

    def rank_hands(self):
        ranked = []
        hand_types = ['high card', 'one pair', 'two pair', 'three of a kind',
                      'full house', 'four of a kind', 'five of a kind']
        for hand_type in hand_types:
            next_type = [hand for hand in self.hands if hand.is_hand_type(hand_type)]
            ranked += sorted(next_type)

        return ranked
    
    def calculate_total_winnings(self):
        total = 0
        
        ranked_hands = self.rank_hands()
        for i, hand in enumerate(ranked_hands):
            total += (i+1) * hand.bid

        return total

    
if __name__ == '__main__':
    CC = CamelCards()
    print(CC.calculate_total_winnings())  # correct: 253473930