import math
import pytest
import calculator

@pytest.mark.parametrize("x, y, expected", [
    [-1, -1, -2],
    [1, 1, 2],
    [1, 0, 1],
    ["Hello ", "World", "Hello World"]
])
def test_add_exact(x, y, expected):
    assert calculator.add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    [0.1, 0.2, 0.3],
    [-0.1, 0.2, 0.1],
    [1.1, -2.2, -1.1]
])
def test_add_floats(x, y, expected):
    tolerance = 1e-14

    actual = calculator.add(x, y)

    assert abs(actual - expected) < tolerance

@pytest.mark.parametrize("x, y", [
    ["Hello", 5],
    [5, "Hello"],
    [True, 0]
])
def test_add_fails_for_incompatible_types(x, y):
    with pytest.raises(TypeError):
        calculator.add("Hello", 5)

@pytest.mark.parametrize("x, expected", [
    [7, math.factorial(7)],
    [1, math.factorial(1)],
    [0, math.factorial(0)]
])
def test_factorial(x, expected):
    assert calculator.factorial(x) == expected

@pytest.mark.parametrize("x, N, expected", [
    [2, 5, math.sin(2)],
    [2, 4, math.sin(2)],
    [0, 0, 0]
])
def test_sin(x, N, expected):
    tolerance = 1e-4

    actual = calculator.sin(x, N)

    assert abs(actual - expected) < tolerance

@pytest.mark.parametrize("x, y, expected", [
    [2, 1, 2],
    [1, 2, 0.5],
    [100, 4, 25]
])
def test_divide(x, y, expected):
    assert calculator.divide(x, y) == expected

@pytest.mark.parametrize("x", [-1, 0, 1])
def test_divide_by_zero_fails(x):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(x, 0)

@pytest.mark.parametrize("x, y, expected", [
    [5, 2, 10],
    [1, 1, 1],
    [7, 0, 0]
])
def test_multiply(x, y, expected):
    assert calculator.multiply(5, 2) == 10

@pytest.mark.parametrize("x, y, expected", [
    [2, 4, -2],
    [4, 2, 2],
    [1, -1, 2]
])
def test_subtract(x, y, expected):
    assert calculator.subtract(x, y) == expected
