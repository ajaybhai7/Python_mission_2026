# Write a function to remove a given word in a list and strip it at the same time

def rem(l, word):
    for item in l :
        return l.strip(word)
n = input("Enter word to remove : ")
l = [1, 4, 2, 5, "Ajay", "Arun"]
print(l, n)