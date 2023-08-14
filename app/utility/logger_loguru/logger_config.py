from loguru import logger


def filtro_de_senha(record):
    if record["message"].lower().startswith("senha"):
        return False
    return True


def configure_logger():
    # Add a handler for a file with a custom filter
    logger.add(
        "logs/logging_loguru.log",
        format="{time} {level} {message} {module} {function} {line}",
        level="DEBUG",
        filter=filtro_de_senha,
    )
