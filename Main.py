# MADE BY HASH6
import random
max_guesses = 5
guesses = 0
number = random.randint(1, 100)
while guesses < max_guesses:
    guess = int(input("guess the number: "))
    if number == guess:
        print("Congratulations! You guessed the number.")
        break
    elif number > guess:
        print("The number is bigger!")
    else:
        print("The number is smaller!")
    guesses += 1
    guesses_left = max_guesses - guesses
    print(f"You have {guesses_left} guesses left.")
else:
    print(f"Sorry, you did not guess the number in {max_guesses} tries. The number was {number}.")
