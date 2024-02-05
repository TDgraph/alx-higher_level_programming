#!/usr/bin/python3

def safe_division(a, b):
    """Safely performs the division of a by b and prints the result.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        The result of the division, or None if division by zero or type error occurs.
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Result of the division: {}".format(result))
    return (result)
