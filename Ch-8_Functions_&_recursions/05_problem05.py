# Write a function which converts inches to centimeters(cms)

def inc_cem(n):
    if n == 0:
        return
    return n * 2.54
n = int(input("Enter Enches to converts in CMS : "))
print(f"The corresponding value in cms is {inc_cem(n)}")

