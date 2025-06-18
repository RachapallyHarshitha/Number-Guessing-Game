import random
print("Welcome to the Number Guessing Game!")
low = 1
high = 50
secret_number = random.randint(low, high)
while True:
    guess = int(input(f"Guess a number between {low} and {high}: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right!")
        break
