# this is one of the projects i first coded: printing pictures. This project was so fun
import random

def roll_dice():
    while True:
        response = input("Do you want to roll the dice? (y/n): ").lower()
        if response != "y":
            break
        
        no = random.randint(1, 6)
        
        print_dice(no)
        
def print_dice(number):
    if number == 1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")
    elif number == 2:
        print("---------")
        print("| 0     |")
        print("|       |")
        print("|     0 |")
        print("---------")
    elif number == 3:
        print("---------")
        print("| 0     |")
        print("|   0   |")
        print("|     0 |")
        print("---------")
    elif number == 4:
        print("---------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("---------")
    elif number == 5:
        print("---------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("---------")
    elif number == 6:
        print("---------")
        print("| 0   0 |")
        print("| 0   0 |")
        print("| 0   0 |")
        print("---------")

if __name__ == "__main__":
    roll_dice()