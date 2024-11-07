import logging

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."

def repl():
    print("Simple Calculator REPL")
    print("Available commands: add, subtract, multiply, divide, or 'exit' to quit.")
    
    while True:
        user_input = input("Enter command: ").strip().lower()
        
        if user_input == "exit":
            print("Exiting calculator. Goodbye!")
            break
        
        # Split the input into parts
        parts = user_input.split()
        
        if len(parts) != 3:
            print("Invalid command. Please enter an operation followed by two numbers.")
            continue
        
        command, x, y = parts[0], parts[1], parts[2]
        
        try:
            x, y = float(x), float(y)
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue
        
        if command == "add":
            result = add(x, y)
        elif command == "subtract":
            result = subtract(x, y)
        elif command == "multiply":
            result = multiply(x, y)
        elif command == "divide":
            result = divide(x, y)
        else:
            print("Unknown command. Available commands: add, subtract, multiply, divide.")
            continue
        
        print("Result:", result)

# Run the REPL
if __name__ == "__main__":
    repl()
