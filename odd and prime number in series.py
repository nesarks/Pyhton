def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

for num in range(lower, upper + 1):
    if num % 2 != 0:
        if is_prime(num):
            print(num)