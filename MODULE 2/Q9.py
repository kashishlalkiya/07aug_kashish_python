#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
n1 = int(input("first integer: "))
n2 = int(input("second integer: "))
n3 = int(input("third integer: "))

if n1 == n2 or n2 == n3 or n1 == n3:
    print("values are equal sum is zero")
    sum = 0
else:
    sum = n1 + n2 + n3

print(f"The sum is: {sum}")