"""Testing the messy function."""

from my_package.messy import messy_function


def test_addition():
    """Testing addition of two numbers."""
    assert messy_function(2, 3) == 5
