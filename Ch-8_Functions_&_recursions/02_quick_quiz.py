# Write a program to greet a user with "Good Day" using function.

def greet():
    Name = input("Enter you'r name: ")
    print(f"Good Day {Name}")

greet()

# in another way

def greet(name):
    print("Good Day" +  name)

greet("Ajay")