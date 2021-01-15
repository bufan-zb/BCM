import logging


def get_logger(path="root.log"):
    logging.basicConfig(
        # filename=path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%m/%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)
    return logger
