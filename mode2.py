import random

guesses = 0
number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = input("Guess the number: ")
    if not guess.isnumeric():
        print("Enter a number!")
        continue
    guess = int(guess)
    if number == guess:
        print(f"Congratulations! You guessed the number in {guesses + 1} guesses.")
        print("You got it!")
        break
    if number > guess:
        print("The number is bigger!")
    else:
        print("The number is smaller!")
    guesses += 1