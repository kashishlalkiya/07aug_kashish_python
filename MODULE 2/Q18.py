#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.
user = input("Enter a string: ")

if len(user) >= 3:
    if user.endswith('ing'):
        string = user + 'ly'
    else:
        string = user + 'ing'
else:
    string = user

print(f"string is: {string}")