# Sum and Average of Natural Numbers

n = int(input("Enter the value of n: "))

# Initialize Variables
sum = 0
average = 0

# Loop through the Natural Numbers
for i in range(1, n+1):
    sum += i

# Calculate Average
average = sum / n

# Print the Results
print("Sum of Natural Numbers up to", n, "is", sum)
print("Average of Natural Numbers up to", n, "is", average)