import logging

logging.basicConfig(
    filename="./access.log",
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt='%Y-%m-%d  %H:%M:%S %a'
)

logging.info("start application.....")

class Logger:

    def debug(self,msg):
        logging.debug(msg)


    def info(self,msg):
        logging.info(msg)


    def error(self,msg):
        logging.error(msg)
