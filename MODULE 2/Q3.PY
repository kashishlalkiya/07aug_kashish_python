#Write a Python program to get the Fibonacci series of given range.
n = int(input("Enter the range: "))

if n < 0:
    print("Invalid range.")
else:
    n1, n2 = 0, 1

    print("Fibonacci series:")
    for _ in range(n + 1):
        print(n1, end =" ")
        next_num = n1 + n2
        n1, n2 = n2, next_num