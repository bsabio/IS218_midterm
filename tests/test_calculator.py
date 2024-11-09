import os
import pytest
from unittest.mock import patch
import pandas as pd

# Adjust sys.path to include the src directory
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import load_plugins, calculator_with_history
from history_manager import initialize_history, save_history, add_to_history, clear_history

# Constants for test
TEST_HISTORY_FILE = os.path.join(os.path.dirname(__file__), "test_calculation_history.csv")

# Fixtures for setup and teardown
@pytest.fixture
def setup_history():
    # Setup: Create a fresh history DataFrame for testing
    history_df = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
    yield history_df
    # Teardown: Remove test history file if created
    if os.path.exists(TEST_HISTORY_FILE):
        os.remove(TEST_HISTORY_FILE)


def test_initialize_history():
    # Test initializing a history file
    history_df = initialize_history(TEST_HISTORY_FILE)
    assert isinstance(history_df, pd.DataFrame)
    assert history_df.empty


def test_save_and_load_history(setup_history):
    # Test saving and loading history
    history_df = add_to_history(setup_history, "add", 3, 4, 7)
    save_history(history_df, TEST_HISTORY_FILE)

    # Reload the history and check content
    loaded_history = pd.read_csv(TEST_HISTORY_FILE)
    assert not loaded_history.empty
    assert loaded_history.iloc[0]['result'] == 7


def test_clear_history():
    # Test clearing the history
    history_df = initialize_history(TEST_HISTORY_FILE)
    history_df = add_to_history(history_df, "add", 3, 4, 7)
    save_history(history_df, TEST_HISTORY_FILE)

    # Clear the history by providing the correct file path
    cleared_history = clear_history(TEST_HISTORY_FILE)  # Pass the file path, not the DataFrame
    assert cleared_history.empty
    assert not os.path.exists(TEST_HISTORY_FILE)


def test_load_plugins():
    # Ensure plugins are loaded correctly
    plugins = load_plugins()
    assert isinstance(plugins, dict)
    # Example: check if certain commands (plugins) exist (assuming 'add' plugin exists in your plugins folder)
    assert "add" in plugins
    assert "subtract" in plugins
