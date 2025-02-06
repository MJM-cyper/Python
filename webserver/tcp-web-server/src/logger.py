import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(client_ip)s - - [%(asctime)s +0000] "%(method)s %(url)s HTTP/1.1" %(http_status)s %(response_size)s', "%d/%b/%Y:%H:%M:%S")
    file_handler = logging.FileHandler("server.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


