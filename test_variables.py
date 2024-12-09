# test_variables.py
import pytest
from variables import sum_of_numbers, greet_user

def test_sum_of_numbers():
    assert sum_of_numbers() == 15, "Expected sum of 5 and 10 to be 15"

def test_greet_user():
    assert greet_user("Alice") == "Hello, Alice!", "Expected greeting to be 'Hello, Alice!'"
    assert greet_user("Bob") == "Hello, Bob!", "Expected greeting to be 'Hello, Bob!'"
