import random
import os

from pip._vendor.distlib.compat import raw_input

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


def hit(deck):
    card = deck.pop()  # The pop() method removes the item at the given index from the list and returns the removed item
    if card == 1:
        card = 'A'
    if card == 11:
        card = 'J'
    if card == 12:
        card = 'Q'
    if card == 13:
        card = 'K'
    return card


if __name__ == "__main__":
    print("Hello, Welcome to Blackjack.\n\n")
    name = raw_input("Enter your name to begin: ")

    game = raw_input(f"Hello, {name}. Type 'S' to start and 'R' to run away: ").lower()
    if game == 's':
        print('\n\nDealing...')
        while game == 's':
            dealerHand = deal(deck)
            playerHand = deal(deck)
            print(f"The dealer shows:\n{dealerHand[0]}")
            print(f'Here are your cards:\n{playerHand[0]}\n{playerHand[1]}')

            decision = raw_input("Type 'H' to hit and 'S' to stand.").lower()
            while decision == 'h':
                playerHand.append(hit(deck))
                print(f"The dealer shows:\n{dealerHand[0]}\n{dealerHand[1]}")
                print(f'Your cards:\n')
                for card in playerHand:
                    print(f'{card} \n')
                decision = raw_input("Type 'H' to hit and 'S' to stand.").lower()
            if decision == 's':
                print(f"The dealer shows:\n{dealerHand[0]}\n{dealerHand[1]}")
                print(f'Your cards:\n{playerHand[0]}\n{playerHand[1]}')

            playAgain = raw_input("Would you like to play again?")



