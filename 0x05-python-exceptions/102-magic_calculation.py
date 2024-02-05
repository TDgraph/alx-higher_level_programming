#!/usr/bin/python3
def magic_calculation(a, b):
    """
    Perform a magic calculation based on the values of 'a' and 'b'.
    
    Args:
        a (int): An integer representing a parameter for the calculation.
        b (int): An integer representing another parameter for the calculation.
        
    Returns:
        int: The result of the magic calculation.
    """
    try:
        if a < 1 or b < 1:
            raise ValueError('Invalid input values')
        
        result = 0
        for i in range(1, 3):
            if i > a:
                result = b + a
                break
            else:
                result += a ** b / i
    except ValueError as ve:
        print(f"ValueError: {ve}")
        result = None
        
    return result
