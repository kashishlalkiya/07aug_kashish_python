#Write a Python program to count the occurrences of each word in a given sentence
sent = input("Enter a sentence: ")

sent_lower = sent.lower()

words = sent_lower.split()

word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Word frequencies:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")