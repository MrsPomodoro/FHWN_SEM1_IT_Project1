"""
Simple Calculator - Main Program
Fill in the missing parts!
"""
from calculator import add, subtract, multiply, divide
from history import save_calculation, load_history, show_history

def show_menu():
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Quit")

def get_numbers():
    """Get two numbers from user with error handling"""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Please enter valid numbers!")
        return None, None

def main():
    while True:
        show_menu()
        choice = input("Choose (1-6): ")
        
        if choice == '6':
            print("Goodbye!")
            break
        elif choice == '5':
            show_history()
        elif choice in ['1', '2', '3', '4']:
            a, b = get_numbers()
            if a is not None and b is not None:
                # TODO: Call the right function based on choice
                # TODO: Save the calculation to history
                pass
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
