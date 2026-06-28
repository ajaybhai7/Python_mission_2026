'''
1 for snake 
-1 for Water
0 for gun
'''
import random

computer = random.choice([-1,0,1])
youstr = input("Enter you choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
reverseddict = {1: "s", -1: "w", 0: "g"}
you = youdict[youstr]

print(f"You choose: {reverseddict[you]}\ncomputer choose: {reverseddict[computer]}")

if computer == you:
    print("It's a draw")

else:
    if computer == -1 and you == 0:
        print("===you loose===")
    
    elif computer == 1 and you == -1:
        print("===you loose===")
    
    elif computer == 0 and you == 1:
        print("===you loose===")

    else:
        print("===you win===")
