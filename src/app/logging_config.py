import logging


from app.config import config


_NO_DEBUG_LIBS = [
        'pika',
        ]

formatter = logging.Formatter(
    '[%(asctime)s %(name)s:%(levelname)s] %(message)s')


def _set_console_log(logger, log_level):
    console = logging.StreamHandler()
    console.setLevel(log_level)
    console.setFormatter(formatter)
    logger.addHandler(console)


def _load_config_file(logger, log_filename, log_level):
    if log_filename is None:
        logger.warning('No LOG_FILE configured')
        return

    logfile = logging.FileHandler(filename=log_filename)
    logfile.setLevel(log_level)
    logfile.setFormatter(formatter)
    logger.addHandler(logfile)


def _set_no_debug_libs():
    for lib in _NO_DEBUG_LIBS:
        logger = logging.getLogger(lib)
        logger.setLevel(logging.INFO)


_lvl = logging._checkLevel  # TODO: implement a proper case insensitive parser
_root_logger = logging.getLogger()
_root_logger.setLevel(_lvl(config.LOG_CONSOLE_LEVEL))
_set_console_log(_root_logger, _lvl(config.LOG_CONSOLE_LEVEL))
_load_config_file(_root_logger, config.LOG_FILE, _lvl(config.LOG_FILE_LEVEL))
_set_no_debug_libs()
