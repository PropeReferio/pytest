import math
import pytest

def test_sqrt_failure(sqrt_value):
    num = 25
    assert math.sqrt(sqrt_value) == 7

def test_square_failure():
    num = 7
    assert 7*7 == 40

def test_equality_failure():
    assert 10 == 11
