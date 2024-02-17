#Write a Python program to test whether a passed letter is a vowel or not
str = input("Enter a letter: ").lower()  
    
if str.isalpha() and len(str) == 1:
    if str in "aeiou":
        print(f"{str} is a vowel.")
    else:
        print(f"{str} is not a vowel.")
else:
    print("Invalid input.")