"""
Calculator functions
Complete these functions!
"""

def add(a, b):
    """Add two numbers"""
    # TODO: Return a + b
    pass

def subtract(a, b):
    """Subtract b from a"""
    # TODO: Return a - b
    pass

def multiply(a, b):
    """Multiply two numbers"""
    # TODO: Return a * b
    pass

def divide(a, b):
    """Divide a by b, handle division by zero"""
    if b == 0:
        return "Error: Cannot divide by zero"
    # TODO: Return a / b
    pass

# Test your functions here
if __name__ == "__main__":
    print("Testing calculator functions...")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")