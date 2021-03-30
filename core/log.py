import logging

def get_logger():
    logger = logging.getLogger('logger')
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s > in %(filename)s, line %(lineno)s')
    streamHandler = logging.StreamHandler()

    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)
    logger.setLevel(logging.DEBUG)

    return logger