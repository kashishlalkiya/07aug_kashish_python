#Write a Python function to reverses a string if its length is a multiple of 4.
user = input("Enter a string: ")

if len(user) % 4 == 0:
    result = user[::-1]
    print(f"reversed string is: {result}")
else:
    print(f"it is not multiple of 4. original string is: {user}")