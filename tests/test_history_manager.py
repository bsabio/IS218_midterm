import os
from unittest.mock import patch
import pandas as pd
import pytest
from history_manager import (
    initialize_history, 
    save_history, 
    add_to_history, 
    display_history, 
    clear_history
)

HISTORY_FILE_TEST = "src/history_manager_test.csv"

@pytest.fixture
def empty_history_df():
    """Fixture to create an empty DataFrame with the correct columns."""
    return pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

@pytest.fixture(autouse=True)
def cleanup_test_file():
    """Remove the test CSV file if it exists after each test."""
    yield
    if os.path.exists(HISTORY_FILE_TEST):
        os.remove(HISTORY_FILE_TEST)

def test_initialize_history_with_no_file():
    history_df = initialize_history(HISTORY_FILE_TEST)
    assert history_df.empty
    assert list(history_df.columns) == ["operation", "operand1", "operand2", "result"]

def test_initialize_history_with_existing_file(empty_history_df):
    # Save an initial history DataFrame to simulate existing history file
    initial_df = add_to_history(empty_history_df, "add", 1, 2, 3)
    save_history(initial_df, HISTORY_FILE_TEST)

    # Load history from the existing file and check contents
    history_df = initialize_history(HISTORY_FILE_TEST)
    assert not history_df.empty
    assert history_df.iloc[0]["operation"] == "add"
    assert history_df.iloc[0]["operand1"] == 1
    assert history_df.iloc[0]["operand2"] == 2
    assert history_df.iloc[0]["result"] == 3

def test_save_history(empty_history_df):
    history_df = add_to_history(empty_history_df, "subtract", 5, 3, 2)
    save_history(history_df, HISTORY_FILE_TEST)
    
    # Verify that the CSV file was created and contains the correct data
    loaded_df = pd.read_csv(HISTORY_FILE_TEST)
    assert not loaded_df.empty
    assert loaded_df.iloc[0]["operation"] == "subtract"
    assert loaded_df.iloc[0]["operand1"] == 5
    assert loaded_df.iloc[0]["operand2"] == 3
    assert loaded_df.iloc[0]["result"] == 2

def test_add_to_history(empty_history_df):
    history_df = add_to_history(empty_history_df, "multiply", 3, 4, 12)
    assert len(history_df) == 1
    assert history_df.iloc[0]["operation"] == "multiply"
    assert history_df.iloc[0]["operand1"] == 3
    assert history_df.iloc[0]["operand2"] == 4
    assert history_df.iloc[0]["result"] == 12

@patch('builtins.print')
def test_display_history(mock_print, empty_history_df):
    # Test empty history display
    display_history(empty_history_df)
    mock_print.assert_called_once_with("No history available.")

    # Test display with some history
    history_df = add_to_history(empty_history_df, "divide", 10, 2, 5)
    display_history(history_df)
    mock_print.assert_called_with(history_df)

def test_clear_history(empty_history_df):
    # Create a file to test clearing history
    initial_df = add_to_history(empty_history_df, "add", 1, 2, 3)
    save_history(initial_df, HISTORY_FILE_TEST)
    
    # Clear the history and check that the file was removed and DataFrame is empty
    cleared_df = clear_history(HISTORY_FILE_TEST)
    assert cleared_df.empty
    assert not os.path.exists(HISTORY_FILE_TEST)
    assert list(cleared_df.columns) == ["operation", "operand1", "operand2", "result"]

