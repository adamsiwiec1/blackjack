import random
import os

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4


def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()  # The pop() method removes the item at the given index from the list and returns the removed item
        if card == 1:
            card = 'A'
        if card == 11:
            card = 'J'
        if card == 12:
            card = 'Q'
        if card == 13:
            card = 'K'
        hand.append(card)
    return hand


hand = deal(deck)

print(hand[0])
print(hand[1])
