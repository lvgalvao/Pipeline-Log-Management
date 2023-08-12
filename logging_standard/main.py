from logging import basicConfig, DEBUG
from logger_config import configure_logger
from operations import division

logger = basicConfig(
    level=DEBUG,
    encoding="utf-8",
    format="%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s",
    handlers=configure_logger(),
)

if __name__ == "__main__":
    division(2, 0)
    division(2, 2)
    division(2, "dois")
