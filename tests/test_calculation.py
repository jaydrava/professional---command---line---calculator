import pytest
from app.calculation.calculation import Calculation, CalculationFactory
from app.operation import operations

def test_calculation_add():
    calc = Calculation(4, 5, operations.Addition.calculate)
    assert calc.get_result() == 9

def test_calculation_subtract():
    calc = Calculation(10, 4, operations.Subtraction.calculate)
    assert calc.get_result() == 6

def test_calculation_factory_add():
    calc = CalculationFactory.create_calculation(4, 5, "+")
    assert calc.get_result() == 9

def test_calculation_factory_invalid_operator():
    with pytest.raises(ValueError):
        CalculationFactory.create_calculation(4, 5, "%")