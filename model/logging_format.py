"""
This module just contains logging format details
"""

import logging
import sys

from pathlib import Path
from logging import getLogger, StreamHandler, Formatter


def set_log_file(logger, props, file):
    logger.setLevel(logging.INFO)
    handler_format = Formatter('%(asctime)s %(process)d %(filename)s %(levelname)s %(message)s')
    stream_handler = StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(handler_format)
    logger.addHandler(stream_handler)
    file_handler = logging.FileHandler(Path(props.main_folder).joinpath(props.cob).joinpath(file))
    file_handler.setFormatter(handler_format)
    logger.addHandler(file_handler)
    return
