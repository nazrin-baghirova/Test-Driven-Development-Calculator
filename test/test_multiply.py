import pytest

from src.calculator import multiply


def test_multiply_two_integers():
  assert multiply(2, 2) == 4


def test_multiply_int_and_float():
  assert multiply(2, 3.5) == 7


def test_multiply_float_and_float():
  assert multiply(2.0, 5.0) == 10.0


def test_multiply_float_and_zero():
  assert multiply(2.2, 0) == 0


def test_multiply_int_and_list():
  with pytest.raises(TypeError):
    assert multiply(19, [])


def test_multiply_neg_int_and_float():
  assert multiply(-1, 5.5) == -5.5


def test_multiply_int_and_float_with_string():
  assert multiply("2", "5.") == 10.


def test_multiply_int_and_zero_with_string():
  assert multiply("5", "0") == 0


def test_multiply_string_and_int():
  with pytest.raises(TypeError):
    assert multiply("Salam", 2)
