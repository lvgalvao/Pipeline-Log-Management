from logging import (
    Formatter,
    Filter,
    INFO,
    FileHandler,
    StreamHandler,
    basicConfig,
    DEBUG,
)


class MeuFiltro(Filter):
    def filter(self, record):
        if record.msg.lower().startswith("senha"):
            return False
        return True


def configure_handlers():
    # Define the formatter
    format_file_handler = Formatter(
        "%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s"
    )

    # Configure file handler
    file_handler = FileHandler(filename="logs/logging_standard.log", mode="w")
    file_handler.setLevel(INFO)
    file_handler.setFormatter(format_file_handler)
    file_handler.addFilter(MeuFiltro())

    # Configure stream handler
    stream_handler = StreamHandler()

    return [file_handler, stream_handler]


def configure_logger():
    # Configure the logger using basicConfig
    basicConfig(
        level=DEBUG,
        encoding="utf-8",
        format="%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s",
        handlers=configure_handlers(),
    )
