rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

print("Welcome to my Rock, Paper and Scissors Game")

print("")

print("Use this game to determine a winner among friends")

print("")

print("To begin you will have to enter 0 , 1 or 2")

print("0 = Rock, 1 = Paper, 2 = Scissors")

ans = [rock,paper,scissors]

user = int(input("Enter your value: "))
computer = random.randint(0,2)

if user == 0 and computer == 2:
    print("You choose :")
    print(ans[user])

    print("Computer choose:")
    print(ans[computer])

    print("You win")

elif user == 1 and computer == 0:
    print("You choose :")
    print(ans[user])

    print("Computer choose:")
    print(ans[computer])

    print("You win")

elif user == 2 and computer == 1:
    print("You choose :")
    print(ans[user])

    print("Computer choose:")
    print(ans[computer])

    print("You win")

elif user == computer:
    print("You choose :")
    print(ans[user])

    print("Computer choose:")
    print(ans[computer])

    print("Draw")

else:
    print("You choose :")
    print(ans[user])

    print("Computer choose:")
    print(ans[computer])

    print("You lose")

