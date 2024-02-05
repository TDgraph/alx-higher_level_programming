#!/usr/bin/python3

def print_elements_safely(some_list=[], elements_to_print=0):
    """Print a specified number of elements from a list.

    Args:
        some_list (list): The list from which to print elements.
        elements_to_print (int): The number of elements to print from some_list.

    Returns:
        The number of elements actually printed.
    """
    elements_printed = 0
    for i in range(elements_to_print):
        try:
            print("{}".format(some_list[i]), end="")
            elements_printed += 1
        except IndexError:
            break
    print("")
    return (elements_printed)
