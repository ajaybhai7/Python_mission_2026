''' The game() function in a program lets a user play a game and
return the score as an integer. you need to read a file 
"High-score.txt" which is either blank or contains the previous
high-score. you need to write a program to update the high-score
whenever the game() function breaks the Hi-score. 
 '''

import random

# def game():
score = random.randint(1, 100)
print("You are Playing.....")

with open("Hiscore.txt") as f:
    hiscore = f.read()
    # if(hiscore != ""):
    hiscore = int(hiscore)
    print(hiscore, type(hiscore))
    #     else:
    #         hiscore == 0

    # print(f"You Score is: {score}")
    # if (score > hiscore):
    #     with open("Hiscore.txt", "w") as f:
    #         f.write(str(hiscore))

    # return score

game()