import logging


def debug(name: str, *msg: [str]):
    logging.getLogger(str(name)).debug(" ".join(msg))


def info(name: str, *msg: [str]):
    logging.getLogger(str(name)).info(" ".join(msg))


def warn(name: str, *msg: [str]):
    logging.getLogger(str(name)).warning(" ".join(msg))


def warning(name: str, *msg: [str]):
    logging.getLogger(str(name)).warning(" ".join(msg))


def critical(name: str, *msg: [str]):
    logging.getLogger(str(name)).critical(" ".join(msg))


def empty():
    logging.getLogger(" ").info("")


__all__ = ["debug", "info", "warn", "warning", "critical"]
