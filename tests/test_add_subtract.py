from src.calculator import add, subtract


def test_add_positive():
    assert add(2, 3) == 5


def test_subtract_negative_result():
    assert subtract(2, 5) == -3

def test_add_zero():
    assert add(0, 5) == 5