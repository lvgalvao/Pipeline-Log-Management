from logging import getLogger

logger = getLogger(__name__)


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            logger.info(f"Chamando a função: {func.__name__}")
            result = func(*args, **kwargs)
            logger.info(f"Finalizando a função: {func.__name__}")
            return result
        except Exception as e:
            # Aqui, registramos a exceção que ocorreu
            logger.error(f"Ocorreu um erro na função {func.__name__}: {str(e)}")
            raise  # Re-lança a exceção para que ela possa ser tratada em outro lugar

    return wrapper
