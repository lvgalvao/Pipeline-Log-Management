from utility.logger_sentry.logger_config import logger_config
from service.transformation import division

if __name__ == "__main__":
    logger_config()
    division(2, 0)
    division(2, 2)
    division(2, "dois")
