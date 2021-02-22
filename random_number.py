import random

number = input("\nPick a number between 1 and 20: ")
number = int(number)
x = random.randint(1, 20)
if number == x:
    print("Amazing, you guessed correclty")
else:
    print("Unlucky, better luck next time")
