import random 

TOOL_NAME = "Number Guesssing Game"

def run():
    print("Welcome to the Number Guessing Game!")

    correct_number = 25

    while True:
        guess = int(input("Guess the number: "))

        if guess < correct_number:
            print("Too Low!")
        elif guess > correct_number:
            print("Too High")
        else:
            print(f"Correct! You guessed the right number!")
            break