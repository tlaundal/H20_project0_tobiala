import math
import calculator

def test_add():
    assert calculator.add(1, 2) == 3

def test_add_floats():
    expected = 0.3
    tolerance = 1e-14

    actual = calculator.add(0.1, 0.2)

    assert abs(actual - expected) < tolerance

def test_add_strings():
    assert calculator.add("Hello ", "World") == "Hello World"

def test_factorial():
    assert calculator.factorial(7) == math.factorial(7)

def test_sin():
    expected = math.sin(2)
    tolerance = 1e-4

    actual = calculator.sin(2, 5)

    assert abs(actual - expected) < tolerance

def test_divide():
    assert calculator.divide(10, 2) == 5

def test_multiply():
    assert calculator.multiply(5, 2) == 10

def test_subtract():
    assert calculator.subtract(2, 4) == -2
