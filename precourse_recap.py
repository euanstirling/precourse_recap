# pick a number between 1 and 20

number = input("\nPick a number between 1 and 20: ")

number = int(number)
if number == 10:
    print(f"Well done, {number} is the correct number")
elif number == 9 or number == 11:
    print("So close, Better luck next time")
else:
    print("Nice try but not correct, better luck next time")
