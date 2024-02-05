#!/usr/bin/python3

def divide_lists_elementwise(list1, list2, length):
    """Divides elements of two lists, element by element.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        length (int): The number of elements to divide.

    Returns:
        A new list of length 'length' containing the result of element-wise divisions.
    """
    result_list = []
    for i in range(0, length):
        try:
            division_result = list1[i] / list2[i]
        except TypeError:
            print("TypeError: Cannot divide non-numeric types.")
            division_result = 0
        except ZeroDivisionError:
            print("ZeroDivisionError: Division by zero encountered.")
            division_result = 0
        except IndexError:
            print("IndexError: Lists are not of equal length.")
            division_result = 0
        finally:
            result_list.append(division_result)
    return (result_list)
