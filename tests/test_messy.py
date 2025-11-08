"""Testing the messy function."""

from my_package.messy import messy_function, multiply


def test_addition():
    """Testing addition of two numbers."""
    assert messy_function(2, 3) == 5


def test_multiplication():
    """Testing multiplication of two numbers."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
