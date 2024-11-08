import pandas as pd
import os

# Path to the history CSV file
HISTORY_FILE = "src/history_manager.csv"

# Initialize an empty DataFrame or load existing history from CSV
def initialize_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)
    else:
        return pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

# Save the history DataFrame to a CSV file
def save_history(history_df):
    history_df.to_csv(HISTORY_FILE, index=False)

# Add a new calculation to the history DataFrame
def add_to_history(history_df, operation, operand1, operand2, result):
    new_entry = {"operation": operation, "operand1": operand1, "operand2": operand2, "result": result}
    return pd.concat([history_df, pd.DataFrame([new_entry])], ignore_index=True)

# Display the calculation history
def display_history(history_df):
    if history_df.empty:
        print("No history available.")
    else:
        print(history_df)

# Clear the history (Delete the CSV file and reset DataFrame)
def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    return pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
