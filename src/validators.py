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
