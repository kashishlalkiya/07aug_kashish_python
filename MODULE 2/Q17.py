#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1 = input("first string: ")
str2 = input("second string: ")

if len(str1) >= 2 and len(str2) >= 2:
    new_string = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
    
    print(f"new string: {new_string}")
else:
    print("enter 2 characters.")