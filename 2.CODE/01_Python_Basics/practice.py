# Single line comment
"""
This is a multi-line comment
Works in .py files
"""

# Case sensitivity
name = "Krish"
Name = "Nick"
print("Lowercase name:", name)
print("Uppercase Name:", Name)

# Indentation example
age = 32
if age > 30:
    print("Age is greater than 30")
print("This line is outside the if block")

# Line continuation
total = 1 + 2 + 3 + 4 + \
        5 + 6 + 7
print("Total:", total)

# Multiple statements on one line
x = 5; y = 10; z = x + y
print("z =", z)

# Type inference (dynamic typing)
var = 10
print("Type of var:", type(var))

var = "Now I'm a string!"
print("Type of var:", type(var))


# Variable declaration and assignment
age = 32
height = 6.1
name = "Krish"
is_student = True

print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Name:", name, "| Type:", type(name))
print("Is student:", is_student, "| Type:", type(is_student))

# Naming conventions: valid vs invalid
first_name = "Krish"   # valid
_last_name = "Nick"    # valid
# 1age = 25            # invalid, starts with number
# first-name = "X"     # invalid, dash not allowed

# Type conversion
age = 25
age_str = str(age)  # int → str
print("Converted:", age_str, "| Type:", type(age_str))

height = 5.9
print("Int conversion:", int(height))   # float → int

# Dynamic typing
var = 10
print(var, type(var))
var = "Hello"
print(var, type(var))
var = 3.14
print(var, type(var))

# Input example
age_input = int(input("Enter your age: "))
print("You entered:", age_input, "| Type:", type(age_input))

# Simple calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)


# Integers
age = 35
print(type(age))  # <class 'int'>

# Floats
height = 5.11
print(type(height))  # <class 'float'>

# Strings
name = "Krish"
print(type(name))  # <class 'str'>

# Booleans
is_true = True
print(type(is_true))  # <class 'bool'>

# Common Error
result = "hello" + 5   # ❌ TypeError

# Fix with typecasting
result = "hello" + str(5)  # ✅ "hello5"
print(result)
