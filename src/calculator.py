from .validators import check_supported_operand_types


@check_supported_operand_types
def add(num1, num2):
  return num1 + num2


@check_supported_operand_types
def subtract(num1, num2):
  return num1 - num2

@check_supported_operand_types
def multiply(num1, num2):
  return num1*num2
