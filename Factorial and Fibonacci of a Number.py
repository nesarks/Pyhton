# Factorial and Fibonacci of a Number

# Factorial (Iterative)
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Factorial (Recursive)
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

# Fibonacci (Iterative)
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

# Fibonacci (Recursive)
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Input from User
number = int(input("Enter a Number: "))

# Factorial (Iterative)
print("Factorial (Iterative) of", number, "is", factorial_iterative(number))

# Factorial (Recursive)
print("Factorial (Recursive) of", number, "is", factorial_recursive(number))

# Fibonacci (Iterative)
print("Fibonacci (Iterative) of", number, "is", fibonacci_iterative(number))

# Fibonacci (Recursive)
print("Fibonacci (Recursive) of", number, "is", fibonacci_recursive(number))