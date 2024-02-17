#Write a Python program to count occurrences of a substring in a string.
str = input("main string: ")

str1 = input("substring to count: ")

occurrences = str.count(str1)

print(f"The substring '{str1}' occurs {occurrences} times in the main string.")