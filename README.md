# IS218_midterm

# Calculator Project

This project is a command-line calculator with plugin support and calculation history management, built in Python. The calculator allows users to perform basic operations such as addition, subtraction, multiplication, and division, and also supports custom operations through a plugin system.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, and division.
- **Plugin System**: Dynamically load additional operations from Python modules in the `plugins` directory.
- **Calculation History**: View, save, and clear calculation history using `pandas` DataFrames.
- **Logging**: Logs plugin loading and calculation actions for easy debugging.
- **Unit Testing and Code Quality**: Comprehensive tests with `pytest` and `pytest-cov` for code coverage, `pylint` for code quality, and GitHub Actions for automated CI/CD.

## Project Structure

- **src/**: Contains the core calculator code and plugin loader.
- **tests/**: Includes unit tests for the main calculator functions, plugin system, and history management.
- **plugins/**: Directory for custom operation modules that can be loaded into the calculator.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/calculator-project.git
   cd calculator-project
