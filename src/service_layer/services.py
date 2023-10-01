from src.domain.model import allocate
from typing import Union
from src.service_layer.validators import check_second_operand_is_zero
from src.domain.converter import convert_model_types


def add(first_operand: Union[int, float],
        second_operand: Union[int, float]) -> Union[int, float]:
  number = allocate(first_operand, second_operand)
  return number.first_operand + number.second_operand


def subtract(first_operand: Union[int, float],
             second_operand: Union[int, float]) -> Union[int, float]:
  number = allocate(first_operand, second_operand)
  return number.first_operand - number.second_operand


def multiply(first_operand: Union[int, float],
             second_operand: Union[int, float]) -> Union[int, float]:
  number = allocate(first_operand, second_operand)
  return number.first_operand * number.second_operand


@convert_model_types
@check_second_operand_is_zero
def divide(first_operand: Union[int, float],
           second_operand: Union[int, float]) -> Union[int, float]:
  number = allocate(first_operand, second_operand)
  return number.first_operand / number.second_operand
