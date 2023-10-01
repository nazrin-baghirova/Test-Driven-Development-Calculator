import pytest
from src.service_layer.services import add
from src.domain.exceptions import UnsupportedModelTypeException


def test_add_two_integers():
  assert add(5, 6) == 11


def test_add_int_and_float():
  assert add(5, 5.5) == 10.5


def test_and_int_and_zero():
  assert add(5, 0) == 5


def test_add_float_and_zero():
  assert add(5.5, 0) == 5.5


def test_add_negative_int_and_int():
  assert add(-5, 5) == 0


def test_add_int_and_list():
  with pytest.raises(UnsupportedModelTypeException):
    assert add(5, [])


def test_add_list_and_list():
  with pytest.raises(UnsupportedModelTypeException):
    assert add([], [])


def test_add_int_and_float_with_string():
  assert add("5", "15.5") == 20.5


def test_add_int_and_zero_with_string():
  assert add("5", "0") == 5


def test_add_string_and_int():
  with pytest.raises(UnsupportedModelTypeException):
    assert add("Salam", 0)
