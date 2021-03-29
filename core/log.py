import logging

def __get_logger():
    __logger = logging.getLogger('logger')
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s > in %(filename)s, line %(lineno)s')
    streamHandler = logging.StreamHandler()

    streamHandler.setFormatter(formatter)
    __logger.addHandler(streamHandler)
    __logger.setLevel(logging.DEBUG)

    return __logger