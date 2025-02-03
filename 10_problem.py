#Write a Python program to calculate the sum of digits of a given number.

num = int(input("Enter a number: "))

sum_of_digit = 0

while num > 0 :
    digit = num % 10 
    sum_of_digit += digit
    num = num // 10

print("Sum of digits: ", sum_of_digit)
