# Guessing Game
# CIS261
# John Marquez
import random
from sys import set_coroutine_origin_tracking_depth
def guessing_game():
    limit = int(input("Enter the limit for the random number (e.g., 100"))
    secret_number = random.randint(1, limit) 
    Print ("Welcome to my guessing game")
    print ("Try to guess the secret number between 1 and {limit},")
    attempts = 0
    while true:
        guess = int(imput("Enter your guess: "))
        attempts += 1
        
    if guess < secret_number:
        print ("Too low, guess again.")
    elif guess > secret_number:
        print ("Too High, guess again.")
    else:
        print(f"Congratulations, you guessed the secret number {secret_number} in {attempts} attempts.")
        
    play_again =("Do you want to play again (Yes or No): ").lower()
    if play_again == 'yes':
        guessing_game()
    