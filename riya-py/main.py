import random

number = random.randint(1, 100)
attempts = 0

print("🎮 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess < number:
            print("Too low! Try a bigger number.")
        elif guess > number:
            print("Too high! Try a smaller number.")
        else:
            print(f"🎉 Correct! The number was {number}.")
            print(f"You guessed it in {attempts} attempts!")
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")