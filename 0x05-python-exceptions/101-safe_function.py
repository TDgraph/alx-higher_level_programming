from __future__ import print_function
import sys

def execute_safely(function, *arguments):
    """Executes a function with given arguments safely.

    Args:
        function (function): The function to execute.
        arguments (tuple): The arguments to pass to the function.

    Returns:
        The result of the function execution if successful, otherwise None.
    """
    try:
        result = function(*arguments)
    except Exception as e:
        print("Error: {}".format(e), file=sys.stderr)
        return None
    else:
        return result
