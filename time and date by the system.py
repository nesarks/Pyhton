# Display Time and Date from System and User Input

import datetime

# Display System Time and Date
print("System Time and Date:")
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Input from User
date_input = input("Enter Date (YYYY-MM-DD): ")
time_input = input("Enter Time (HH:MM:SS): ")

# Display User Input Time and Date
print("User Input Time and Date:")
print(f"{date_input} {time_input}")