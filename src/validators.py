from functools import wraps

def check_second_operand_is_zero(func_):

  @wraps(func_)
  def wrapper(num1, num2):
    if num2 == 0:
      raise ZeroDivisionError("Division by zero is not supported")
    return func_(num1, num2)

  return wrapper
