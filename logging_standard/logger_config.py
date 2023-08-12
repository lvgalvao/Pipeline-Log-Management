from logging import Formatter, Filter, INFO, FileHandler, StreamHandler


class MeuFiltro(Filter):
    def filter(self, record):
        if record.msg.lower().startswith("senha"):
            return False
        return True


def configure_logger():
    format_file_handler = Formatter(
        "%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s"
    )

    file_handler = FileHandler(filename="logs/logging_standard.log", mode="w")
    file_handler.setLevel(INFO)
    file_handler.setFormatter(format_file_handler)
    file_handler.addFilter(MeuFiltro())

    stream_handler = StreamHandler()

    handlers = [file_handler, stream_handler]

    return handlers
