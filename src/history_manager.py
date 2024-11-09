import pandas as pd
import os

# Path to the history CSV file
HISTORY_FILE = "src/history_manager.csv"

# Initialize an empty DataFrame or load existing history from CSV
def initialize_history(file_path=None):
    if file_path and os.path.exists(file_path):
        # Load history from file if it exists
        return pd.read_csv(file_path)
    else:
        # Create an empty DataFrame if no history file exists
        return pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

# Save the history DataFrame to a CSV file
def save_history(history_df, file_path):
    history_df.to_csv(file_path, index=False)

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
def clear_history(history_file):
    """Clear the history and return an empty DataFrame."""
    if os.path.exists(history_file):
        os.remove(history_file)
    return pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
    # Return an empty DataFrame with predefined columns