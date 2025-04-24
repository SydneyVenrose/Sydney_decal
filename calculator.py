import math_tools

# Ask the user for two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Ask the user for the operation
operation = input("Choose operation (add, subtract, multiply, divide): ").lower()

# Perform the chosen operation
if operation == "add":
    result = math_tools.add(a, b)
elif operation == "subtract":
    result = math_tools.subtract(a, b)
elif operation == "multiply":
    result = math_tools.multiply(a, b)
elif operation == "divide":
    result = math_tools.divide(a, b)
else:
    result = "Invalid operation."

print("Result:", result)
