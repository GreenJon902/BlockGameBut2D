import logging
import os

import appdirs

import App.logger as _logger

name = "BlockGameBut2D"
author = "GreenJon902"
version = "0.0.1"

user_data_dir = appdirs.user_data_dir(appname=name, appauthor=author, version=version)
log_dir = appdirs.user_log_dir(appname=name, appauthor=author, version=version)
log_path = str(os.path.join(log_dir, str(len(os.listdir(log_dir))))) + ".log"


def logger_setup():
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(levelname)7s: %(name)30s: %(message)s")

    handler = logging.FileHandler(filename=log_path)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(formatter)
    logger.addHandler(consoleHandler)

    _logger.info("Logger", "Logger saving at", str(log_path))
