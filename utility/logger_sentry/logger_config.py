import os
from dotenv import load_dotenv
import sentry_sdk
from logging import basicConfig, DEBUG
from sentry_sdk.integrations.logging import LoggingIntegration


def logger_config():
    sentry_logging = LoggingIntegration(level=DEBUG, event_level=DEBUG)

    load_dotenv()

    DSN = os.getenv("DSN")

    sentry_sdk.init(
        dsn=DSN,
        integrations=[sentry_logging],
        traces_sample_rate=1.0,
    )
