# Write a program to find out the line number where python
# is present from ques 6.

with open("log.txt", "r")as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    print(f"Yes python is present. Line no: {line}")
    lineno = lineno + 1
    break
else:
    print("Python is not present")