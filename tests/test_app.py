import sys
import os
from io import StringIO

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import add  # Now the import should work
from app import main #Import main

def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_mixed_numbers():
    assert add(5, -2) == 3


def test_add_zero():
    assert add(10, 0) == 10

def test_main_execution(capsys):
    main()
    captured = capsys.readouterr()
    assert "The result of 5 + 3 is: 8" in captured.out
