import sys

def print_integer_safely(value):
    """Prints an integer using "{:d}".format().

    If a ValueError occurs, a corresponding message
    is printed to the standard error.

    Args:
        value (int): The integer to print.

    Returns:
        If printing is successful - True.
        If a TypeError or ValueError occurs during printing - False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print(f"Exception: {e}", file=sys.stderr)
        return (False)
