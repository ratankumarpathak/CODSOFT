num1 = float(input("Enter the first number: ")) 
operation = input("Choose an operation (+, -, *, /): ")  
num2 = float(input("Enter the second number: "))  
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("You can't divide by zero!")  
    else:
        result = num1 / num2
else:
    print("Invalid operation. Please use +, -, *, or /")
    result = None  
if operation in ["+", "-", "*", "/"] and not (operation == "/" and num2 == 0):
    print("The result is:", result)

