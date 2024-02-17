#Write a Python program to count the number of characters (character frequency) in a string
user = input("Enter a string: ")

frequency = {}

for char in user:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequencies:")
for char, frequency in frequency.items():
    print(f"{char}: {frequency}")