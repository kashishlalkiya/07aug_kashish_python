#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
n1 = int(input("first integer: "))
n2 = int(input("second integer: "))

if n1 == n2 or n1 + n2 == 5 or abs(n1 - n2) == 5:
    result = True
else:
    result = False

print(result)