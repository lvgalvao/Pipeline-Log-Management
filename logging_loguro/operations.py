from loguru import logger


def division(x, y):
    logger.info("inicio")
    try:
        result = x / y
        logger.info("fim")
    except ZeroDivisionError:
        logger.error("Não é possível dividir por 0")
        return 0
    except TypeError:
        logger.error("senha")
        return 0
    return result
