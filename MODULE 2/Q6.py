# Write python program that swap two number with temp variable and without temp variable.
# Swap with temp variable
n1 = float(input("first number: "))
n2 = float(input("second number: "))
print(f"Original numbers: n1 = {n1}, n2 = {n2}")
temp = n1
n1 = n2
n2 = temp
print(f"Swapped numbers (with temp): n1 = {n1}, n2 = {n2}")

# Swap without temp variable
n1 = float(input("first number: "))
n2 = float(input("second number: "))
print(f"Original numbers: n1 = {n1}, n2 = {n2}")
n1, n2 = n2, n1
print(f"Swapped numbers (without temp): n1 = {n1}, n2 = {n2}")