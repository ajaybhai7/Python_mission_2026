'''
Write a program to generate multiplication table from 2 to 20
and write it to the new different file in a folder for a 
13 years old.. '''

def multy(n, i):
    n = 1
    i = 1
    while i > 10:
        return print(f"{n} x {i} = {n*i}")
    i = i+1
    if i == 10:
        return (1, 10)

multy()
    # with open("table.txt", "w") as file:
#     file.write()
    
