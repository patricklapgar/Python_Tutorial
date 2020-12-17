import random

# This is a simple guessing game where the player inputs a number
# but must guess a higher or lower number to win

random_number = random.randint(1, 10)

while True:
    guess = print("Guess a number between 1 and 10:\n")
    guess = int(guess)
    if guess < random_number:
        print("TOO LOW!!")
    elif guess > random_number:
        print("TOO HIGH!!")
    else:
        print("YOU WON!!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("Thanks, bye!!")
            break

