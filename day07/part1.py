import sys
import re
from functools import cmp_to_key

rx = re.compile(r'\d+')

d = {100: 'five of a kind', 90: 'four of a kind', 70: 'full house', 60: 'three of a kind', 50:'two pair', 40: 'one_pair', 10: 'hgh card'}
def is_five_of_a_kind(hand):
    counts = [hand.count(card) for card in set(hand)]
    return len(set(hand)) == 1

def is_four_of_a_kind(hand):
    counts = [hand.count(card) for card in set(hand)]
    return (4 in counts and 1 in counts)

def is_full_house(hand):
    counts = [hand.count(card) for card in set(hand)]
    return (3 in counts and 2 in counts)

def is_three_of_a_kind(hand):
    counts = [hand.count(card) for card in set(hand)]
    return (3 in counts and len(set(hand)) == 3)

def is_two_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    return (counts.count(2) == 2 and counts.count(1) == 1)

def is_one_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    return (counts.count(2) == 1 and counts.count(1) == 3)

def classify_hand(hand):
    if is_five_of_a_kind(hand):
        return 100
    elif is_four_of_a_kind(hand):
        return 90
    elif is_full_house(hand):
        return 70
    elif is_three_of_a_kind(hand):
        return 60
    elif is_two_pair(hand):
        return 50
    elif is_one_pair(hand):
        return 40
    else:
        return 10

def order_poker_hands(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def hand_value(hand):
        values = [card_values[card] for card in hand]
        # values.sort(reverse=True)
        return values


    value1 = hand_value(hand1)
    value2 = hand_value(hand2)

    classification1 = classify_hand(hand1)
    classification2 = classify_hand(hand2)

    if classification1 != classification2:
        return classification1 - classification2

    for v1, v2 in zip(value1, value2):
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1

    return 0


x = sys.stdin.read().strip().split('\n')
x = [k.split(' ') for k in x]

for a in x:
    a[0] = list(a[0])
    a[1] = int(a[1])

x.sort(key=cmp_to_key(order_poker_hands))

total = 0
for i,h in enumerate(x):
    bid = h[1]*(i+1)
    total += bid
print(total)
