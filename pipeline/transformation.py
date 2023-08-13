from log_standard.logger_decorator import logger_decorator
from logging import error


@logger_decorator
def division(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        error("Não é possível dividir por 0")
        return 0
    except TypeError:
        error("Não é possível dividir por string")
        return 0
    return result
