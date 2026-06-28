'''
Write a program to generate multiplication table from 2 to 20
and write it to the new different file in a folder for a 
13 years old.. '''

i = 1
n = 1
while i < 11:
    print(f"{n} x {i} = {i*n}")
    i = i+1
    if i == 11:
        n += 1
        print(f"{n} x {i} = {i*n}")
        i = i+1
# with open("table.txt", "w") as file:
#     file.write()
    
