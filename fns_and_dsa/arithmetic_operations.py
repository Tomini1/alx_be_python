def perform_operation(num1, num2, operation):
    """performs basic arithmetic operations: add, subtract, multiply, divide. """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else: 
        return "Error: Invalid operation."
