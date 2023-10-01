from src.domain.model import allocate
from typing import Union
from src.service_layer.validators import check_second_operand_is_zero
from src.domain.converter import convert_model_types
from src.actions_layer.actions import handle_number_actions

def add(first_operand: Union[int, float],
        second_operand: Union[int, float]) -> Union[int, float]:
  return handle_number_actions("add", allocate(first_operand, second_operand))()


def subtract(first_operand: Union[int, float],
             second_operand: Union[int, float]) -> Union[int, float]:
  return handle_number_actions("subtract", allocate(first_operand, second_operand))()


def multiply(first_operand: Union[int, float],
             second_operand: Union[int, float]) -> Union[int, float]:
  return handle_number_actions("multiply", allocate(first_operand, second_operand))()


@convert_model_types
@check_second_operand_is_zero
def divide(first_operand: Union[int, float],
           second_operand: Union[int, float]) -> Union[int, float]:
  return handle_number_actions("divide", allocate(first_operand, second_operand))()
