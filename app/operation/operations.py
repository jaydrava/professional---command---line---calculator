# operations.py

from unittest import result


class Addition:
    """ Handles addition of multiple numbers. """
    
    @staticmethod
    
    def calculate(*values):
        # Adds all values passed and returns the result.
        return sum(values)
    
class Subtraction:
    """ Handles subtraction of multiple numbers. """
    
    @staticmethod
    def calculate(*values):
        # Start with the first value and subtract all subsequent values.
        result = values[0]
        for val in values[1:]:
            result -= val
        return result
    
class Multiplication:
    """ Handles multiplication of multiple numbers. """
    
    @staticmethod
    def calculate(*values):
        # multiplies all values passed and returns the result.
        result = 1
        for val in values:
            result *= val
        return result
    
class Division:
    """ Handles division of multiple numbers. """
    
    @staticmethod
    def calculate(*values):
        # divides the first value by all subsequent values.
        result = values[0]
        for val in values[1:]:
            if val == 0:
                raise ZeroDivisionError("Division by zero is not allowed.") # pragma: no cover
            result /= val
        return result