''' A file contains a word "Donkey" multiple times. You need to
write a program which replace this word with #### by updating
the same file'''


with open("file.txt") as f:
    file = f.read()
if "Donkey" in file:
    f.write("####")
