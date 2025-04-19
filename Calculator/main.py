from art import logo

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

def process(num1):
    num2 = float(input("Please enter number 2: "))

    for x in operations:
        print(x)

    symbol = input("Please type you operation from the list above: ")
    result = operations[symbol](num1, num2)
    return result , symbol , num2

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}

print(logo)

num1 = float(input("Please enter number 1: "))
num2 = float(0)
symbol = ""
looping = True

while looping == True:
    output ,symbol ,num2 = process(num1)
    print(f"The result of {num1} {symbol} {num2} = {output}")
    action = input(f"if you would like to continue with number: {output} then type 'y' or type'n' to end the program: ")
    if action == "n":
        print("Thank you for using this program")
        looping = False
    elif action == "y":
        num1 = output
    