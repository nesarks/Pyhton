a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
print("Smallest:", smallest)
print("Largest:", largest)