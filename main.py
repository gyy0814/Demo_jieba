import ORDP
import logging
LOG_FORMAT = "[%(asctime)s] [%(levelname)s L%(lineno)s]:%(message)s "
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
ORDP.scan()