import os
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def bids():
    name = input("Please enter your name: ")
    bid = input("Please enter your bid: ")
    bid_member[name] = int(bid)

print(logo)
bid_member = {}
bids()
highest_bid = 0
winner = ""
print(highest_bid)

choice = input("Press 'y' if there are other bidders or press 'n' if there are none ")

while choice == "y":
    clear()
    bids()
    print(bid_member)
    choice = input("Press 'y' if there are other bidders or press 'n' if there are none ")

for x in bid_member:
    if bid_member[x] > highest_bid:
        highest_bid = bid_member[x]
        winner = x
print(f"The person with the highest bid of {highest_bid} is {winner}")



