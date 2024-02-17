#Write a Python program to get the Factorial number of given number.
n = int(input("Enter a number: "))

if n < 0:
    print("negative numbers not defined.")
else:
    result = 1
    for i in range(1, n + 1):
        result *= i

    print(f"factorial of {n} is {result}")