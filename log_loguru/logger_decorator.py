from loguru import logger


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando a função: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Finalizando a função: {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Ocorreu um erro na função {func.__name__}: {str(e)}")
            raise e

    return wrapper
