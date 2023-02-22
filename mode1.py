import random

max_guesses = int(input("Enter the maximum number of guesses: "))
guesses = 0
number = random.randint(1, 100)

while guesses < max_guesses:
    guess = input("Guess the number: ")
    if not guess.isnumeric():
        print("Enter a number!")
        continue
    guess = int(guess)
    if number == guess:
        print(f"Congratulations! You guessed the number in {guesses + 1} guesses.")
        print("Say a number!")
        break
    if number > guess:
        print("The number is bigger!")
    else:
        print("The number is smaller!")
    guesses += 1
    guesses_left = max_guesses - guesses
    print(f"You have {guesses_left} guesses left.")
else:
    print(f"Sorry, you did not guess the number in {max_guesses} tries. The number was {number}.")