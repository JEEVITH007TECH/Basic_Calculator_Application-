def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error Doesn't Divisible by zero"
    elif operation == '**':
        return num1 ** num2    
    else:
        return "Invalid operation selection"

print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select the operation:")
print("( + , - , * , / , ** )")
operation = input("Enter operation: ")

result = calculate(num1, num2, operation)
print(f"Result: {result}")
