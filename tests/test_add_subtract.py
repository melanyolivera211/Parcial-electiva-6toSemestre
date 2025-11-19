from src.calculator import add, subtract


def test_add_positive():
    assert add(2, 3) == 7


def test_subtract_negative_result():
    assert subtract(2, 5) == -3
