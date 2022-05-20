import logging


def logging_define():
    logger = logging.getLogger('stress monitoring')
    logger.setLevel(logging.DEBUG)
    logStream = logging.StreamHandler()
    logStream.setLevel(logging.DEBUG)

    logFile = logging.FileHandler('datset.log')
    logFile.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logStream.setFormatter(formatter)
    logFile.setFormatter(formatter)
    logger.addHandler(logStream)
    logger.addHandler(logFile)
    return logger
