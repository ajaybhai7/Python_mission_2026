a = 90 # globle variable

def fun():
    global a
    a = 2

    print(a)

fun() #Local variable
print(a)