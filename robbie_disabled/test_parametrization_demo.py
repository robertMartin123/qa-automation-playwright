import pytest


def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Only numeric values allowed")
    return a * b



@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (5, 0, 0),
    (-1, 5, -5),
    (-3, -3, 9),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a,b", [
        ("2", 3),
        (None, 5),
])
def test_multiply_invalid_inputs(a, b):
    with pytest.raises(TypeError):
        multiply(a, b)

import math
import pytest


@pytest.mark.parametrize("a,b", [
    (0, 5),
    (1, -1),
    (1_000_000, 2),
    (0.0, 3.5),
    (0.1, 9.0),
        (0,0)
])
def test_multiply_boundary_values(a, b):
    assert multiply(a, b) == a * b

def test_multiply_nan_behavior():
    result = multiply(float("nan"), 5)
    assert math.isnan(result)
