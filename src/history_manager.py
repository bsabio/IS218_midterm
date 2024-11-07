import pandas as pd
import os

# Path to the history CSV file
HISTORY_FILE = "calculation_history.csv"

# Initialize an empty DataFrame for history
def initialize_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)
    else:
        return pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

# Save history to CSV
def save_history(history_df):
    history_df.to_csv(HISTORY_FILE, index=False)

# Add a calculation to history
def add_to_history(history_df, operation, operand1, operand2, result):
    new_entry = {"operation": operation, "operand1": operand1, "operand2": operand2, "result": result}
    history_df = history_df.append(new_entry, ignore_index=True)
    return history_df

# Clear the history
def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    return pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

# Display history
def display_history(history_df):
    if history_df.empty:
        print("No history available.")
    else:
        print(history_df)

# Example usage within a calculator function
def calculator_with_history():
    history_df = initialize_history()
    
    while True:
        user_input = input("Enter command (or type 'history', 'clear', 'exit'): ").strip().lower()
        
        if user_input == "exit":
            save_history(history_df)
            print("Goodbye!")
            break
        elif user_input == "history":
            display_history(history_df)
        elif user_input == "clear":
            history_df = clear_history()
            print("History cleared.")
        else:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Enter in format: operation operand1 operand2")
                continue
            
            operation, operand1, operand2 = parts[0], parts[1], parts[2]
            try:
                operand1, operand2 = float(operand1), float(operand2)
            except ValueError:
                print("Please enter valid numbers.")
                continue

            if operation == "add":
                result = operand1 + operand2
            elif operation == "subtract":
                result = operand1 - operand2
            elif operation == "multiply":
                result = operand1 * operand2
            elif operation == "divide":
                if operand2 == 0:
                    print("Error: Division by zero.")
                    continue
                result = operand1 / operand2
            else:
                print("Unknown operation.")
                continue
            
            print("Result:", result)
            history_df = add_to_history(history_df, operation, operand1, operand2, result)
