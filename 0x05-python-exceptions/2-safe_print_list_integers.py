#!/usr/bin/python3

def print_first_x_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): The list from which to print elements.
        x (int): The number of elements from my_list to print.

    Returns:
        The number of elements actually printed.
    """
    elements_printed = 0  # Counter for elements printed
    for i in range(0, x):  # Iterate through the first x elements
        try:
            # Try to print the element as an integer
            print("{:d}".format(my_list[i]), end="")
            elements_printed += 1  # Increment the counter if successful
        except (ValueError, TypeError):
            continue  # Continue to the next element if an error occurs
    print("")  # Print a newline after printing the elements
    return (elements_printed)  # Return the number of elements printed
