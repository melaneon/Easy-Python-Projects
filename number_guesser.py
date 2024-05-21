import random

top_of_range = input("Type a number: ")
guesses = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()

else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You guessed the number!")
        break
    elif user_guess > random_number:
        print("You are above the number")
    else:
        print("You are below the number")

print(f"You guessed it in {guesses} guess(es)")

