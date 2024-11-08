import importlib
import os
import sys
import logging
from history_manager import (
    initialize_history, 
    save_history, 
    add_to_history, 
    display_history, 
    clear_history
)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Ensure plugins folder is on path
sys.path.append(os.path.join(os.path.dirname(__file__)))

# Plugin loader: loads plugins from the plugins directory
def load_plugins():
    plugins = {}
    plugin_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # Remove ".py" from filename
            module_path = f"plugins.{module_name}"
            try:
                module = importlib.import_module(module_path)
                if hasattr(module, 'run') and hasattr(module, 'name'):
                    plugins[module.name()] = module.run
                    logging.info(f"Loaded plugin: {module.name()}")
                else:
                    logging.warning(f"Plugin {module_name} is missing 'run' or 'name' function.")
            except ImportError as e:
                logging.error(f"Failed to import plugin {module_name}: {e}")
    return plugins

# Main calculator REPL with plugin support and history management
def calculator_with_history():
    history_df = initialize_history()
    plugins = load_plugins()

    while True:
        user_input = input("Enter command (or 'history', 'clear', 'exit'): ").strip().lower()
        
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
                print("Invalid input. Enter: operation operand1 operand2")
                continue

            operation, operand1, operand2 = parts[0], parts[1], parts[2]
            try:
                operand1, operand2 = float(operand1), float(operand2)
            except ValueError:
                print("Please enter valid numbers.")
                continue

            if operation in plugins:
                try:
                    result = plugins[operation](operand1, operand2)
                    print(f"Result: {result}")
                    history_df = add_to_history(history_df, operation, operand1, operand2, result)
                except Exception as e:
                    logging.error(f"Error in performing {operation}: {e}")
            else:
                print(f"Unknown operation: '{operation}'. Available plugins: {', '.join(plugins.keys())}")

# Run the calculator
if __name__ == "__main__":
    calculator_with_history()
