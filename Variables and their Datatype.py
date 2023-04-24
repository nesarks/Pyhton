 # Variables and their Data Types

# Integer
x = 10
print(type(x)) # <class 'int'>

# Float
y = 10.5
print(type(y)) # <class 'float'>

# Boolean
z = True
print(type(z)) # <class 'bool'>

# String
name = "John"
print(type(name)) # <class 'str'>a

# List
list_var = [1, 2, 3, 4]
print(type(list_var)) # <class 'list'>

# Set
set_var = {1, 2, 3, 4}
print(type(set_var)) # <class 'set'>

# Dictionary
dict_var = {
    "name": "John",
    "age": 30
}
print(type(dict_var)) # <class 'dict'>

# Tuple
tuple_var = (1, 2, 3, 4)
print(type(tuple_var)) # <class 'tuple'>

# Exchange of Two Values
a = 10
b = 20

# Using a Temporary Variable
temp = a
a = b
b = temp

print("a:", a) # a: 20
print("b:", b) # b: 10

# Without Using a Temporary Variable
a, b = b, a

print("a:", a) # a: 10
print("b:", b) # b: 20
