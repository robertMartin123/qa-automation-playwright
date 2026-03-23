import math

def _validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Only numeric values allowed")

    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("Values must be finite numbers")


def add(a, b):
    _validate_numbers(a, b)
    return a + b


def subtract(a, b):
    _validate_numbers(a, b)
    return a - b


def multiply(a, b):
    _validate_numbers(a, b)
    return a * b


def divide(a, b):
    _validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

