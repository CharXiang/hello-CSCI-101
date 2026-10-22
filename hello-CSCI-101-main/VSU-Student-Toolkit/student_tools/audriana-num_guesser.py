import random

def guess_number():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    num = random.randint(1, 100)
    guesses = 0
    guess = int(input("Enter your guess: "))
    while guess != num:
        guesses += 1
        if(guess > num):
            print("Your guess was too high. Try again!")
            guess = int(input("Enter your guess: "))
        elif(guess < num):
            print("Your guess was too low. Try again!")
            guess = int(input("Enter your guess: "))
    guesses += 1
    print(f"Congratulations! You've guessed the number {num} in {guesses} guesses.")
guess_number()