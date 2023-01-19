from art import logo
import random
from os import name, system

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
lives = 10 
exit_ = False
while not exit_:
    clear()
    print(logo)
    print("Welcome to Number Guessing Game!")
    lives
    mode = input("Choose mode [e]asy [h]ard : ").lower()
    if mode == 'h':
        lives = 5
    random_number = random.randint(1,100)
    while lives != 0:
        guess = int(input(f"Guess the number {lives} left :"))
        if guess == random_number:
            print(f"Wow You Guessed the number {random_number} correctly")
            play_again = input("Wanna play again: ")
            if play_again == 'n':
                exit_ = True
            break
        elif guess > random_number:
            print("You've Guessed high")
        elif guess < random_number:
            print("You've Guessed low")
        lives -= 1
    if lives == 0:
        play_again = input("Oops! looks like you've out of lives wanna play again: ")
        if play_again == 'n':
            exit_ = True
        

    
