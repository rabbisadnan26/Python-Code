#Find the Largest of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a>b :
    print(f"{a} number is greater")
elif b<a:
    print(f"{b} number is greater")
else:
    print("Number is negative, zero or other")
