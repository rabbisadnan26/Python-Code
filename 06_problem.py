#Write a Python program to find the largest number among three given numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b and a>c :
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
    
