import random

from reportlab.lib.randomtext import PRINTING

secret_number = random.randint(1,100)
count = 0
while True:
    try:
        guess = int(input("Guess Number between 1 to 100:"))
        count += 1
        if guess>secret_number:
            print("Number is too HIGH!")
        elif guess<secret_number:
            print("Number is too LOW!")
        else :
            print(f"Successfully Guessed! Number is {secret_number}")
            print(f"It took {count} Guesses to Win!")
            break
    except ValueError:
        print("Invalid Input:Give Numbers only")
print("Thanks for Game!")