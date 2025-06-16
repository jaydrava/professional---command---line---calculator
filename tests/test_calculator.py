import builtins
import pytest 
from app.calculator import calculator
from app.calculation.calculation import CalculationFactory
from app.operation.operations import Addition, Subtraction, Multiplication, Division

# This fixture runs automatically before each test to clear calculations history.
@pytest.fixture(autouse=True)
def clear_history():
    """ Clear the calculation history before each test. """
    calculator.calculation_history.clear()  

# Helper function to simulate user inputs in tests.
def mock_inputs(inputs):
    inputs_iter = iter(inputs)
    def input_mock(prompt=""):
        return next(inputs_iter)
    return input_mock

#Group test related to general commands line help,exit, and invalid commands
class TestGeneralCommands:

    def test_help_command(self,capsys, monkeypatch):
        # Test that the help command shows a list of available commands.
        monkeypatch.setattr(builtins, 'input', mock_inputs(['help', 'exit']))
        calculator.run_calculator()
        captured = capsys.readouterr()
        assert "Available commands:" in captured.out
        assert "Exiting the calculator." in captured.out

    def test_exit_command(self,capsys, monkeypatch):
        # Test that the exit command cleanly exits the calculator.
        monkeypatch.setattr(builtins, 'input', mock_inputs(['exit']))
        calculator.run_calculator()
        captured = capsys.readouterr()
        assert "Exiting the calculator." in captured.out

    def test_invalid_command(self,capsys, monkeypatch):
        # Test how calculator handles unknown commands.
        monkeypatch.setattr(builtins, 'input', mock_inputs(['invalid_command', 'exit']))
        calculator.run_calculator()
        captured = capsys.readouterr()
        assert "Invalid command. Type 'help' for a list of commands." in captured.out

# Group test related to arithmetic operations like addition, subtraction, multiplication, and division

class TestArithmeticOperations:

    def test_addition_operation(self,capsys, monkeypatch):
        # Test addition operation with valid inputs.
        monkeypatch.setattr(builtins, 'input', mock_inputs(['+', '3', '4', 'exit']))
        calculator.run_calculator() 
        captured = capsys.readouterr()
        assert "Result: 7.0" in captured.out
        assert "Exiting the calculator." in captured.out
    
    def test_division_by_zero(self,capsys, monkeypatch):
        # Test that division by zero is handled correctly.
        monkeypatch.setattr(builtins, 'input', mock_inputs(['/', '5', '0', 'exit']))
        calculator.run_calculator()
        captured = capsys.readouterr()
        assert "Error: Division by zero is not allowed." in captured.out


    def test_invalid_number_input(self,capsys, monkeypatch):
        # Test input validation: non-numeric values should show error message.
        monkeypatch.setattr(builtins, 'input', mock_inputs(['+', 'a', 'b', 'exit']))
        calculator.run_calculator()
        captured = capsys.readouterr()
        assert "Invalid input. Please enter valid numbers." in captured.out


    def test_invalid_operator(self):
        # Test that an unsupported operator raises a ValueError.
        with pytest.raises(ValueError, match="Unsupported operator: %"):
            CalculationFactory.create_calculation(1, 2, '%')


    def test_invalid_operator_in_calculator(self,capsys, monkeypatch):
        # This goes throught the full calculator loop and triggers the generic exception handling
        monkeypatch.setattr(builtins, 'input',mock_inputs(['%', '1', '2', 'exit']))
        calculator.run_calculator()
        captured = capsys.readouterr()
        assert "Invalid command. Type 'help' for a list of commands." in captured.out


    def test_general_exception(self,capsys, monkeypatch):
        # Test that a general exception in the calculation process is caught and reported.
        def faulty_create_calculation(a, b, operator):
            raise Exception("Forced error")
        monkeypatch.setattr(
            'app.calculation.calculation.CalculationFactory.create_calculation', faulty_create_calculation)
        monkeypatch.setattr(builtins, 'input',mock_inputs(['+', '1', '2', 'exit']))

        calculator.run_calculator()
        captured = capsys.readouterr()
        assert "An error occurred: Forced error" in captured.out

# Group test related to history command and empty history
class TestHistoryCommand:

    def test_history_command(self,capsys, monkeypatch):
        # Test that history shows after some calculations.
        monkeypatch.setattr(builtins, 'input', mock_inputs(['+', '2', '3', 'history', 'exit']))
        calculator.run_calculator()
        captured = capsys.readouterr()
        assert "History of calculations:" in captured.out
        assert "Exiting the calculator." in captured.out
    
    def test_history_empty(self,capsys, monkeypatch):
        # Test that the history command shows proper message when no calculations have been performed.
        calculator.calculation_history.clear()  # Ensure history is empty
        monkeypatch.setattr(builtins, 'input', mock_inputs(['history', 'exit']))
        calculator.run_calculator()
        captured = capsys.readouterr()
        assert "No calculations performed yet." in captured.out
        assert "Exiting the calculator." in captured.out

# Group test for direct operations logic (unit tests without calculator loop)

class TestOperationLogic:

    def test_subtraction_multiple(self):
        assert Subtraction.calculate(10, 2, 3) == 5 # Test subtraction with multiple values

    def test_multiplication_multiple(self):
        assert Multiplication.calculate(2, 3, 4) == 24 # Test multiplication with multiple values

    def test_division_multiple(self):
        assert Division.calculate(100, 2, 5) == 10 # Test division with multiple values

    def test_division_by_zero_exception(self):
        with pytest.raises(ZeroDivisionError): # Test that division by zero raises an exception
            Division.calculate(10, 0)