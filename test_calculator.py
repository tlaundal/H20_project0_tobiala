import calculator

def test_add():
    assert calculator.add(1, 2) == 3

def test_add_floats():
    expected = 0.3
    tolerance = 1e-14

    actual = calculator.add(0.1, 0.2)

    assert abs(actual - expected) < tolerance
