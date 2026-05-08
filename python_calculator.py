# Simple Calculator Program

print("=== Simple Calculator ===")

number1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
number2 = float(input("Enter second number: "))

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid Operator"

print("Result:", result)