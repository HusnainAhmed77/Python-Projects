import os
import random
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def card_shuffle_player():
    global player_sum
    a = random.randint(0,len(cards)-1)
    player_cards.append(cards[a])
    player_sum += cards[a]

def card_shuffle_computer():
    global computer_sum
    a = random.randint(0,len(cards)-1)
    computer_cards.append(cards[a])
    computer_sum += cards[a]

def starting_decks():
    for x in range(2):
        card_shuffle_player()
        card_shuffle_computer()
    
def deck_choice(choice):

    if choice == 'y':
        card_shuffle_player()
        if computer_sum <= 16:
            card_shuffle_computer()

    elif choice == 'n':
        if computer_sum <= 16:
            card_shuffle_computer()
        
    else:
        print("wrong input, start the program again")
        f = input("Enter 'y' if you want to draw a card or 'n' if you don't")
        deck_choice(f)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

loop = True

print(logo)

print("Welcome to my blackjack game ")
print("")

while loop == True:

    player_cards = []

    player_sum = 0

    computer_cards = []

    computer_sum = 0

    starting_decks()

    print(f"The player's deck is {player_cards}")
    print(f"The player's sum is {player_sum}")
    print("")

    print(f"The computer's deck is {computer_cards[0]}")
    
    print("")


    choice = input("Enter 'y' if you want to draw a card or 'n' if you don't")
    deck_choice(choice)

    if player_sum > 21:
        for x in range (len(player_cards)):
            if player_cards[x] == 11:
                player_cards[x] = 1
                player_sum -=10

    if computer_sum > 21:
        for x in range(len(computer_cards)):
            if computer_cards[x] == 11:
                computer_cards[x] = 1
                computer_sum -= 10
    
    print(f"The players deck is {player_cards}")
    print(f"The players sum is {player_sum}")
    print("")

    print(f"The computers deck is {computer_cards}")
    print(f"The computers sum is {computer_sum}")
    print("")

    if computer_sum >= 22 and player_sum >= 22:
        print("Both player and computer lose")
    else:
        if player_sum > computer_sum:
            if player_sum <=21:
                print("player wins")
                print("computer loses")
            else:
                print("Blackjack, you lose")
            
        elif computer_sum > player_sum:
            if computer_sum <=21:
                print("computer wins")
                print("player loses")
            else:
                print("blackjack: computer loses")

        elif computer_sum == player_sum:
            if player_sum <= 21:
                print("Draw, no winner")
        

    loop_choice = input("Enter 'y' if you want to start again or 'n' if you don't")

    if loop_choice == "n":
        loop = False
    elif loop_choice =="y":
        clear()
    else:
        print("Wrong input, restart program")