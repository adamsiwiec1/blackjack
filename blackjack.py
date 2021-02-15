import random
from colorama import Fore, Back, Style, init
from pip._vendor.distlib.compat import raw_input


class Deck:

    def __init__(self, deck=None):
        self.deck = deck

init(autoreset=True)
highcards = ['J', 'Q', 'K']
d1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
d2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 8
d4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 16  # (4*13 = 52 - one deck) (16*13 = 208 - four decks)

deckObj = Deck(d4)

def deal(deck):
    hand = []
    for i in range(2):
        try:
            random.shuffle(deck)
            card = deck.pop()  # The pop() method removes the item at the given index from the list and returns the removed item
        except IndexError or TypeError:
            print("A new deck is being shuffled...")
            random.shuffle(deckObj.deck)
            card = deckObj.deck.pop()
            print("The new deck has been shuffled.")
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


def get_total(hand, ttl=0):
    h = []
    a = []
    for x in hand:
        h.append(x)
        if x == 'A':
            a.append(x)
    hrange = range(len(h))  # Get full range of hand
    arange = range(len(a))  # Get range of aces

    for x in hrange:
        if hand[x] not in highcards and hand[x] != 'A':
            ttl = ttl + int(hand[x])
        if hand[x] in highcards and hand[x] != 'A':
            ttl = ttl + 10
    if len(a) > 0:
        for x in arange:
            if ttl >= 11:
                ttl = ttl + 1
            if ttl < 11:
                ttl = ttl + 11

    return ttl


def print_cards(hand):
    for x in hand:
        print(x)


def find_winner(dlr, plr):
    dealer = get_total(dlr)
    player = get_total(plr)
    if dealer > 21 and player <= 21:
        print(Fore.GREEN + "\nYou won!!!")
    elif dealer > player or player > 21:
        print(Fore.RED + "\nYou lost :(")
    elif player == dealer:
        print(Fore.YELLOW + "\nPush...")
    elif 21 >= player > dealer:
        print(Fore.GREEN + "\nYou won!!!")


def dealer_draw(dealr):
    dealer = get_total(dealr)
    if dealer < 17:
        dealr.append(hit(deckObj.deck))
        return dealr
    if dealer >= 17:
        return dealr


def game_result(dhand, phand):
    print(Fore.MAGENTA + '\nGAME RESULTS:')
    print(Fore.BLUE + 'Dealer')
    print_cards(dhand)
    print(Fore.BLUE + 'Player')
    print_cards(phand)
    find_winner(dhand, phand)


def start_game(userInput):
    playAgain = 'N'
    game = userInput
    if game == 's' or playAgain == 'y':
        print(Fore.LIGHTMAGENTA_EX + '\nDealing...')
        while game == 's':
            total = 0
            dealerHand = deal(deckObj.deck)
            playerHand = deal(deckObj.deck)
            print(Fore.LIGHTWHITE_EX + f"Dealer upcard:\n{dealerHand[0]}")
            playerTotal = get_total(playerHand, total)
            print(Fore.LIGHTWHITE_EX + f'Here are your cards: (Total = {str(playerTotal)})\n{playerHand[0]}\n{playerHand[1]}')
            decision = raw_input(Fore.LIGHTMAGENTA_EX + "Type 'H' to hit and 'S' to stand:").lower()
            while decision == 'h':
                playerHand.append(hit(deckObj.deck))
                playerTotal = get_total(playerHand, total)
                print(Fore.BLUE + 'Dealer upcard:')
                print(dealerHand[0])
                print(Fore.CYAN + f'Your hand: (Total = {str(playerTotal)})')
                print_cards(playerHand)
                if playerTotal == 21:  # Check for win
                    print(Fore.GREEN + "\nAuto-stand.\n")
                    decision = 's'
                if playerTotal > 21:  # Check for loss
                    print(Fore.RED + 'You busted!!')
                    decision = 's'
                if playerTotal < 21:  # Prompt player to Hit/Stand
                    decision = ''
                    choices = ['h', 's']
                    while decision not in choices:
                        decision = raw_input(Fore.LIGHTWHITE_EX + "\nType 'H' to Hit and 'S' to Stand: ").lower()
                        if decision not in choices:
                            print(Fore.RED + "Make a valid selection.")
            if decision == 's':
                # Dealer draws cards after the hand is over.
                while get_total(dealerHand) < 17:  # Dealer hits on 16/stands on 17
                    dealerHand = dealer_draw(dealerHand)

                # Display game result
                game_result(dealerHand, playerHand)

                # Ask the player if they will play another hand - continue/break the loop
                playAgain = raw_input(Fore.LIGHTMAGENTA_EX + "Would you like to play again? (Y/N) ").lower()

                if playAgain == 'y':
                    continue
                if playAgain == 'n':
                    exit(0)
                else:
                    while True:
                        print(Fore.RED + "Please enter a correct input.")
                        playAgain = raw_input(Fore.LIGHTMAGENTA_EX + "Would you like to play again? (Y/N) ").lower()
                        if playAgain == 'n' or 'y':
                            break
    else:
        print(Fore.LIGHTMAGENTA_EX + "Thanks for playing Blackjack!!")


if __name__ == "__main__":
    print(Fore.LIGHTMAGENTA_EX + "Hello, Welcome to Blackjack.")
    name = raw_input(Fore.LIGHTWHITE_EX + "Enter your name to begin: ")
    game = raw_input(Fore.LIGHTMAGENTA_EX + f'Hello, {Fore.CYAN + Style.BRIGHT + str(name)}.' + Fore.LIGHTMAGENTA_EX + Style.NORMAL + " Type 'S' to start and 'R' to run away: ").lower()
    start_game(game)



