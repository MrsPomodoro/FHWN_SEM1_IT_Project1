"""
Calculator functions: add, subtract, multiply, divide.
All functions take two float arguments (a, b) and return a float or error message.
"""

def add(a, b):
    """Add two numbers"""
    try:
        return float(a) + float(b)
    except (ValueError, TypeError):
        return "Error: Both inputs must be numbers."

def subtract(a, b):
    """Subtract b from a"""
    try:
        return float(a) - float(b)
    except (ValueError, TypeError):
        return "Error: Both inputs must be numbers."

def multiply(a, b):
    """Multiply two numbers"""
    try:
        return float(a) * float(b)
    except (ValueError, TypeError):
        return "Error: Both inputs must be numbers."

def divide(a, b):
    """Divide a by b, handle division by zero"""
    try:
        a, b = float(a), float(b)
        if b == 0:
            return "Error: Cannot divide by zero."
        return a / b
    except (ValueError, TypeError):
        return "Error: Both inputs must be numbers."

# Test your functions here
if __name__ == "__main__":
    print("Testing calculator functions...")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"3 * 4 = {multiply(3, 4)}")
    print(f"'a' + 5 = {add('a', 5)}")