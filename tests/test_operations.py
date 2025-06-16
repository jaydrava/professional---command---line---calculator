import pytest
from app.operation import operations

def test_addition():
    assert operations.Addition.calculate(2, 3) == 5

def test_subtraction():
    assert operations.Subtraction.calculate(5, 3) == 2

def test_multiplication():
    assert operations.Multiplication.calculate(4, 3) == 12

def test_division():
    assert operations.Division.calculate(6, 2) == 3

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        operations.Division.calculate(5, 0)