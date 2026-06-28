# Creat a class with a class attribute a; creat an object from it and set 'a'
# direcctly using object.a = 0 does this change the class attribute.

class demo:
    a = 4

o = demo()
print(o.a)
     
o.a = 0
print(o.a)

print(demo.a)
# The Output will be: 
"""
4 first output
0 second output
"""

 