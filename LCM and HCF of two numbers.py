def hcf(a, b):
    if a == 0:
        return b
    return hcf(b % a, a)
def lcm(a, b):
    return (a * b) // hcf(a, b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
h = hcf(a, b)
l = lcm(a, b)
print("HCF:", h)
print("LCM:", l)
