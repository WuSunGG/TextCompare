import logging

logging.basicConfig(
    filename="./access.log",
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt='%Y-%m-%d  %H:%M:%S %a'
)



def debug(msg):
    """
    :return: logging
    """
    return logging.debug(msg)

def info(msg):
    return logging.info(msg)

