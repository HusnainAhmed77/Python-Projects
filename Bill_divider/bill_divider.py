print("Welcome to my bill divider application where you can see how much each person will pay for the total meal")

bill = float(input ("Please enter the total bill amount: $"))

tip = int(input ("Please input how much tip you want to give in percentage 2,5,10, etc: "))

people = int(input ("Please enter how many person to divide this bill into: "))

tip = round((tip / 100) + 1.00, 2)

total = round((bill / people) * tip , 2)

print (f"The total amount to be paid by {people} persons is ${total}.")



