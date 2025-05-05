# Basic Python Program: Greeting and Age in 5 Years

import sys
import os


def get_user_details():
    """Gets user's name and age, handling potential errors."""
    if os.getenv("TEST_ENV") == "true":  # Check for test environment variable
        return "Test User", 30  # Return default values for testing
    while True:
        name = input("Enter your name: ")
        if name:  # Check if name is not empty
            break
        else:
            print("Name cannot be empty. Please enter your name.")
    while True:
        try:
            age = int(input("Enter your age: "))
            if age >= 0:  # Check if age is non-negative
                break
            else:
                print("Age must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")
    return name, age


def calculate_future_age(age, years=5):
    """Calculates age in the future."""
    return age + years


def generate_greeting(name, future_age):
    """Generates the greeting message."""
    return f"Hello, {name}! In 5 years, you'll be {future_age} years old."


if __name__ == "__main__":
    user_name, user_age = get_user_details()
    next_age = calculate_future_age(user_age)
    greeting_message = generate_greeting(user_name, next_age)
    print(greeting_message)


# Example test function (you'd typically put these in a separate test file)
def test_calculate_future_age():
    assert calculate_future_age(25) == 30
    assert calculate_future_age(30, 10) == 40
    assert calculate_future_age(0) == 5