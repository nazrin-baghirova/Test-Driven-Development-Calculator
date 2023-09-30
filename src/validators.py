from functools import wraps


def check_supported_operand_types(func_):

  @wraps(func_)
  def wrapper(num1, num2):
    if not (isinstance(num1, int) or isinstance(num1, float)):
      raise TypeError("Unsupported operand type")
    if not (isinstance(num2, int) or isinstance(num2, float)):
      raise TypeError("Unsupported operand type")
    return func_(num1, num2)

  return wrapper


def check_second_operand_is_zero(func_):

  @wraps(func_)
  def wrapper(num1, num2):
    if num2 == 0:
      raise ZeroDivisionError("Division by zero is not supported")
    return func_(num1, num2)

  return wrapper
