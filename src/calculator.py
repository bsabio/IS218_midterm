import logging
import pandas as pd
import os

# Set up logging configuration (to capture INFO-level logs)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]  # Output logs to the console (could be a file if desired)
)

HISTORY_FILE = "calculation_history.csv"

# Initialize or load history
def initialize_history():
    if os.path.exists(HISTORY_FILE):
        logging.info("Loading history from file.")
        return pd.read_csv(HISTORY_FILE)
    else:
        logging.info("No history found, starting with an empty history.")
        return pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

# Save history to CSV
def save_history(history_df):
    history_df.to_csv(HISTORY_FILE, index=False)
    logging.info("History saved to file.")

def add_to_history(history_df, operation, operand1, operand2, result):
    new_entry = pd.DataFrame([{
        "operation": operation,
        "operand1": operand1,
        "operand2": operand2,
        "result": result
    }])
    history_df = pd.concat([history_df, new_entry], ignore_index=True)
    return history_df


# Calculator with history and logging
def calculator_with_history():
    history_df = initialize_history()

    while True:
        user_input = input("Enter command (or type 'history', 'clear', 'exit'): ").strip().lower()

        if user_input == "exit":
            save_history(history_df)
            logging.info("Exiting calculator.")
            print("Goodbye!")
            break
        elif user_input == "history":
            print(history_df)
        elif user_input == "clear":
            history_df = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
            logging.info("History cleared.")
            print("History cleared.")
        else:
            parts = user_input.split()
            if len(parts) != 3:
                logging.warning("Invalid input format.")
                print("Invalid input. Enter in format: operation operand1 operand2")
                continue

            operation, operand1, operand2 = parts[0], parts[1], parts[2]
            try:
                operand1, operand2 = float(operand1), float(operand2)
            except ValueError:
                logging.warning("Invalid operand value.")
                print("Please enter valid numbers.")
                continue

            # Perform the operation
            if operation == "add":
                result = operand1 + operand2
            elif operation == "subtract":
                result = operand1 - operand2
            elif operation == "multiply":
                result = operand1 * operand2
            elif operation == "divide":
                if operand2 == 0:
                    logging.error("Attempted division by zero.")
                    print("Error: Division by zero.")
                    continue
                result = operand1 / operand2
            else:
                logging.error(f"Unknown operation: {operation}")
                print("Unknown operation.")
                continue

            print("Result:", result)
            history_df = add_to_history(history_df, operation, operand1, operand2, result)

# Run the calculator
if __name__ == "__main__":
    calculator_with_history()
