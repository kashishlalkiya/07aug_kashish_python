#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
user = input("Enter a string: ")

ind_not = user.find('not')
poor = user.find('poor')

if ind_not != -1 and poor != -1 and ind_not < poor:
    string = user[:ind_not] + 'good' + user[poor + 4:]
else:
    string = user

print(f"resulting string is: {string}")