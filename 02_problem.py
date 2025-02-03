# Write a program to swap two numbers 
# without using a third variable.

a = int(input("Enter Number a: ")) # 10
b = int(input("Enter Number b: ")) # 5

a = a + b 
b = a - b 
a = a - b 
print(f"The swapping of a and b is : {a}, {b}")

