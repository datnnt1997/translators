import logging
from pathlib import Path

logger = logging.getLogger()


def init_logger(log_file=None, log_file_level=logging.NOTSET):
    """
    Example:
        >>> init_logger(log_file)
        >>> logger.info("abc'")
    """
    if isinstance(log_file, Path):
        log_file = str(log_file)

    log_format = logging.Formatter(fmt='%(message)s',
                                   datefmt='%m/%d/%Y %H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.handlers = [console_handler]
    if log_file and log_file != '':
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(log_file_level)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    return logger