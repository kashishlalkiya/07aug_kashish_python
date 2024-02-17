#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string
user = input("Enter a string: ")

if len(user) < 2:
    result = ""
else:
    result = user[:2] + user[-2:]

print(f"string is: {result}")