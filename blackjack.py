import random
from colorama import Fore, Back, Style, init
from pip._vendor.distlib.compat import raw_input

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4
init(autoreset=True)
highcards = ['A','J','Q','K']


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


def normalize_hand(hand, ttl=0):
    if 'A' or 'J' or 'Q' or 'K' in hand:
        for x in hand:
            if x in highcards:
                ttl = ttl + 10
            else:
                ttl = ttl + x
    else:
        ttl = 0
        for x in hand:
            ttl = + x

    return ttl


def print_cards(hand):
    for x in hand:
        print(x)


def find_winner(dlr, plr):
    dealer = normalize_hand(dlr)
    player = normalize_hand(plr)
    if dealer > 21 and player <= 21:
        print(Fore.GREEN + "\nYou won!!!")
    elif dealer > player or player > 21:
        print(Fore.RED + "\nYou lost :(")
    elif player == dealer:
        print(Fore.YELLOW + "\nPush...")
    elif 21 >= player > dealer:
        print(Fore.GREEN + "\nYou won!!!")


def dealer_draw(dealr):
    dealer = normalize_hand(dealr)
    if dealer < 17:
        dealr.append(hit(deck))
        return dealr
    if dealer >= 17:
        return dealr


if __name__ == "__main__":
    print(Fore.LIGHTMAGENTA_EX + "Hello, Welcome to Blackjack.")
    name = raw_input(Fore.LIGHTWHITE_EX + "Enter your name to begin: ")
    playAgain = 'N'
    game = raw_input(Fore.LIGHTMAGENTA_EX + f'Hello, {Fore.CYAN + Style.BRIGHT + str(name)}.' + Fore.LIGHTMAGENTA_EX + Style.NORMAL + " Type 'S' to start and 'R' to run away: ").lower()
    if game == 's' or playAgain == 'y':
        print(Fore.LIGHTMAGENTA_EX + '\nDealing...')
        while game == 's':
            dealerHand = deal(deck)
            playerHand = deal(deck)
            print(Fore.LIGHTWHITE_EX + f"The dealer shows:\n{dealerHand[0]}")
            print(Fore.LIGHTWHITE_EX + f'Here are your cards:\n{playerHand[0]}\n{playerHand[1]}')

            decision = raw_input(Fore.LIGHTMAGENTA_EX + "Type 'H' to hit and 'S' to stand.").lower()
            total = 0
            while decision == 'h':
                playerHand.append(hit(deck))
                playerTotal = normalize_hand(playerHand, total)
                print("Your Total: " + str(playerTotal))
                print(Fore.BLUE + 'The dealer shows:')
                print(dealerHand[0])
                print(Fore.CYAN + 'Your hand:')
                print_cards(playerHand)
                if playerTotal == 21:  # Check for win
                    print(Fore.GREEN + "\nAuto-stand.\n")
                    decision = 's'
                if playerTotal > 21:  # Check for loss
                    print(Fore.RED + 'You busted!!')
                    decision = 's'
                if playerTotal < 21:  # Prompt player to Hit/Stand
                    decision = raw_input(Fore.LIGHTWHITE_EX + "\nType 'H' to Hit and 'S' to Stand: ").lower()
            if decision == 's':

                while normalize_hand(dealerHand) < 17:
                    dealerHand = dealer_draw(dealerHand)

                print(Fore.MAGENTA + '\nGAME RESULTS:')
                print(Fore.BLUE + 'Dealer')
                print_cards(dealerHand)
                print(Fore.BLUE + 'Player')
                print_cards(playerHand)
                find_winner(dealerHand, playerHand)
            playAgain = raw_input(Fore.LIGHTMAGENTA_EX + "Would you like to play again? (Y/N) ").lower()



