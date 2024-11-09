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
    if not os.path.exists(plugin_dir):
        os.makedirs(plugin_dir)
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module_path = f"plugins.{module_name}"
            try:
                module = importlib.import_module(module_path)
                if hasattr(module, 'run') and hasattr(module, 'name'):
                    # Register the plugin's command name and function
                    plugins[module.name()] = module.run
                    logging.info(f"Loaded plugin: {module.name()}")
            except ImportError as e:
                logging.error(f"Failed to import plugin {module_name}: {e}")
    return plugins

# Main calculator REPL with plugin support and history management
def calculator_with_history():

    history_df = initialize_history()

    # Load plugins
    plugins = load_plugins()

    while True:
        # Show dynamic menu with available commands
        print("Available commands: add, subtract, multiply, divide, history, clear, exit")
        print("Plugin commands: " + ", ".join(plugins.keys()))
        
        user_input = input("Enter command: ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "history":
            # Display history
            display_history(history_df)
        elif user_input == "clear":
            # Pass history_df to clear_history to clear history correctly
            history_df = clear_history(history_df)  # Fix here!
            print("History cleared.")
        elif user_input in plugins:
            # Execute plugin command
            operand1 = float(input("Enter first operand: "))
            operand2 = float(input("Enter second operand: "))
            try:
                result = plugins[user_input](operand1, operand2)
                print(f"Result of {user_input}: {result}")
                # Save to history
                history_df = add_to_history(history_df, user_input, operand1, operand2, result)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Unknown command. Type 'menu' to see available commands.")

# Run the calculator
if __name__ == "__main__":
    calculator_with_history()
