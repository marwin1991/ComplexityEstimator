import logging

loggers = {}


def init_logger(name):
    global loggers

    if loggers.get(name):
        return loggers.get(name)
    else:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler('calc_complex_logs.log')
        handler.setLevel(logging.DEBUG)

        handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)
        loggers[name]=logger
        return logger
