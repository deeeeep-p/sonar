# Simple Python Program

def add(x, y):
    """Adds two numbers."""
    return x + y

if __name__ == "__main__":
    x = 5  # Use fixed values for demonstration
    y = 3
    result = add(x, y)
    print(f"The result of {x} + {y} is: {result}")

# DO NOT put any input() calls here or anywhere else outside if __name__ == "__main__":