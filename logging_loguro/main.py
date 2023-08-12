from loguru import logger
from operations import division


def filtro_de_senha(record):
    if record["message"].lower().startswith("senha"):
        return False
    return True


# adicionando um handler para um arquivo
logger.add(
    "logs/logging_loguru.log",
    format="{time} {level} {message} {module} {function} {line}",
    level="DEBUG",
    filter=filtro_de_senha,
)

if __name__ == "__main__":
    division(2, 0)
    division(2, 2)
    division(2, "dois")
