from data import data
import random
from art import logo,vs,lost
from os import system, name

score = 0
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
def Higher_Lower(u1_name,u1_fls,u2_name,u2_fls):
    clear()
    print(logo)
    print(f"Your Score: {score}")
    print()
    print(f"Instagram User: {u1_name}")
    print(vs)
    print(f"Instagram User: {u2_name}\n")
    isHigher = u1_fls > u2_fls
    isLower = u1_fls < u2_fls

    userInput = input(f"Does {u1_name} has [h]igher or [l]ower followrs than {u2_name}: ").lower()

    if (userInput == 'h' and isHigher) or (userInput == 'l' and isLower):
        return 0
    else:
        return 2

def main():
    user = random.choice(data)
    user1_name = user["name"]
    user1_followers = user["follower_count"]
    data.remove(user)
    user = random.choice(data)
    user2_name = user["name"]
    user2_followers = user["follower_count"]
    data.remove(user)
    global score
    status = Higher_Lower(user1_name,user1_followers,user2_name,user2_followers)
    while status == 0:
        score +=1
        user1_followers = user2_followers
        user1_name = user2_name 
        user = random.choice(data)
        user2_name = user["name"]
        user2_followers = user["follower_count"]
        data.remove(user)
        
        status = Higher_Lower(user1_name,user1_followers,user2_name,user2_followers)
    if status != 0:
        clear()
        print(lost,'\n')
        print(f"Your final score: {score}")
        play_again = input(f"Oops you lost. Wanna play again [y/n]: ").lower()
        if play_again == 'y':
            score = 0
            main()
        else:
            print("\nThanks for playing, have a good day :)")
            return 0

main()
