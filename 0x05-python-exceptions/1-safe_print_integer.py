#!/usr/bin/python3

def print_safe_integer(value_to_print):
    """Print an integer using the "{:d}".format() method.

    Args:
        value_to_print (int): The integer to print.

    Returns:
        If printing is successful - True.
        If a TypeError or ValueError occurs during printing - False.
    """
    try:
        print("{:d}".format(value_to_print))
        return True
    except (TypeError, ValueError):
        return (False)
