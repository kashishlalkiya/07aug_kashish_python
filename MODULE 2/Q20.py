#Write a Python function that takes a list of words and returns the length of the longest one.
list = ["apple", "banana", "kiwi", "strawberry", "orange"]

if list:
    longest_word = max(list, key=lambda x: len(x))

    print(f"The length: {len(longest_word)}")
else:
    print("list is empty.")