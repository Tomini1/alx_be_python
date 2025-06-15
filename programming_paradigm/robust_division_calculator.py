def safe_divide(numerator, denominator):
    """"safely divide two numbers by first converting inputs to floats"""

    try: 
        # attempting to conert input to float
        n = float(numerator)
        d = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        result = n / d
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    return f"The result of the division is {result}"