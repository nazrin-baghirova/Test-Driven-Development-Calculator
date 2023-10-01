from converters import convert_types
from validators import check_second_operand_is_zero, check_supported_operand_types


@convert_types
@check_supported_operand_types
def add(num1, num2):
  print(type(num1), type(num2))
  return num1 + num2


@convert_types
@check_supported_operand_types
def subtract(num1, num2):
  return num1 - num2


@convert_types
@check_supported_operand_types
def multiply(num1, num2):
  return num1 * num2


@convert_types
@check_supported_operand_types
@check_second_operand_is_zero
def divide(num1, num2):
  return num1 / num2
