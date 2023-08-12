from logging import error, info


def division(x, y):
    info("inicio")
    try:
        result = x / y
        info("fim")
    except ZeroDivisionError:
        error("Não é possível dividir por 0")
        return 0
    except TypeError:
        error("senha")
        return 0
    return result
