import random

from pip._vendor.distlib.compat import raw_input

from blackjack import deal, dealer_draw, print_cards

# deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4
deck = []
userInput = raw_input("Press any key to start and -1 to exit:")
while userInput != '-1':
    dealer = deal(deck)

    print_cards(dealer)
    player = deal(deck)
    print_cards(player)
