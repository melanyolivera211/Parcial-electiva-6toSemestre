import pytest
from src.calculator import mean


def test_mean_ok():
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_empty_error():
    with pytest.raises(ValueError):
        mean([])
