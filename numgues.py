import random
import math

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # User input for range
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    
    # Generating a random number within the range
    random_number = random.randint(lower, upper)
    
    # Calculating the minimum number of guesses using log formula
    min_guesses = math.ceil(math.log2(upper - lower + 1))
    
    print(f"You have to guess the number between {lower} and {upper}.")
    print(f"You should be able to guess it in {min_guesses} tries if you use the optimal strategy.")
    
    attempts = 0
    while True:
        attempts += 1
        guess = int(input("Enter your guess: "))
        
        if guess > random_number:
            print("Try Again! You guessed too high.")
        elif guess < random_number:
            print("Try Again! You guessed too small.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            if attempts == min_guesses:
                print("Great job! You guessed it in the minimum number of attempts.")
            else:
                print("Better luck next time!")
            break

# Run the game
if __name__ == "__main__":
    number_guessing_game()
