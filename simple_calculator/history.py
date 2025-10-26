"""
History management - keep it simple!
"""
import json
import os

HISTORY_FILE = "calculations.json"

def load_history():
    """Load history from file, return empty list if file doesn't exist"""
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r') as file:
                return json.load(file)
        return []
    except:
        print("Could not load history file.")
        return []

def save_calculation(operation, result):
    """Save a calculation to history (keep only last 5)"""
    history = load_history()
    
    # Create new entry
    entry = {
        "operation": operation,
        "result": result
    }
    
    # Add to history
    history.append(entry)
    
    # Keep only last 5 calculations
    if len(history) > 5:
        history = history[-5:]
    
    # Save to file
    try:
        with open(HISTORY_FILE, 'w') as file:
            json.dump(history, file, indent=2)
    except:
        print("Could not save to history file.")

def show_history():
    """Display calculation history"""
    history = load_history()
    
    if not history:
        print("No calculations in history.")
        return
    
    print("\n=== Recent Calculations ===")
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry['operation']} = {entry['result']}")