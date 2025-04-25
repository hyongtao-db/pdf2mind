import logging

logger = logging.getLogger("pdf2mind")

def setup_logger(debug_mode=False):
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG if debug_mode else logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG if debug_mode else logging.INFO)

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger
