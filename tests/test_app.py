from .app import add  # Import the add function from app.py


def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_add_mixed_numbers():
    assert add(5, -2) == 3

def test_add_zero():
    assert add(10, 0) == 10