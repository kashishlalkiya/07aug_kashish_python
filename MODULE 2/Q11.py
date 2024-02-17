#Write a python program to sum of the first n positive integers.
n = int(input("positive integer(n): "))

if n <= 0:
    print("enter positive integer.")
else:
    sum = (n * (n + 1)) // 2

    print(f"The sum of the first {n} positive integers is: {sum}")