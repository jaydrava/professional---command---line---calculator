from app.operation import operations

class Calculation:
    """ Represents a single arithemtic calculation ... """

    def __init__(self, a: float, b: float, operator: callable):
        self.a = a
        self.b = b  
        self.operator = operator
        self.result = self._calculate()
    
    def _calculate(self):
        """ Executes the stored operation using the provided operator. """
        return self.operator(self.a, self.b)
    
    def get_result(self):
        """ Returns the result of the calculation. """
        return self.result
    

class CalculationFactory:
    """ Factory class to create Calculation instances based on the operator. """

    @staticmethod
    def create_calculation(a: float, b: float, operator: str) -> Calculation:
        """ Return a Calculation instance based on the operator provided. """
        operation_map = {
            '+': operations.Addition.calculate,
            '-': operations.Subtraction.calculate,
            '*': operations.Multiplication.calculate,
            '/': operations.Division.calculate
        }
        if operator not in operation_map:
            raise ValueError(f"Unsupported operator: {operator}")   # pragma: no cover
        return Calculation(a, b, operation_map[operator])