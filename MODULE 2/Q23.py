#Write a Python function to insert a string in the middle of a string.
str1 = input("main string: ")
str2 = input("string to insert: ")

middle = len(str1) // 2

result = str1[:middle] + str2 + str1[middle:]

print(f"string is: {result}")