''' The game() function in a program lets a user play a game and
return the score as an integer. you need to read a file 
"High-score.txt" which is either blank or contains the previous
high-score. you need to write a program to update the high-score
whenever the game() function breaks the Hi-score. 
 '''

import random

def game():
    score = random.randint(1, 100)
    print("You are Playing.....")

    with open("High-score.txt") as f:
        high_score = int(f.read())

    print(f"You Score is: {score}")

    if (score > high_score):
        with open("High-score.txt", "w") as f:
            f.write(str(high_score))

    return score


game()