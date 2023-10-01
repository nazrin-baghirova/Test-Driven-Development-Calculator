from functools import wraps


def _convert(value):
  final_value = None
  if isinstance(value, str):
    try:
      final_value = int(value)
    except ValueError:
      final_value = float(value)
    finally:
      return final_value
  return value


def convert_types(func_):

  @wraps(func_)
  def wrapper(num1, num2):
    converted1 = _convert(num1)
    converted2 = _convert(num2)
    return func_(converted1, converted2)

  return wrapper
