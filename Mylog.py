import logging
from datetime import datetime

log = logging.getLogger(__name__)


format = logging.Formatter("%(asctime)s | %(filename)s | %(lineno)s | %(levelname)s -> %(message)s")

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(format)
log.addHandler(streamHandler)

log_path = 'log'

fileHandler = logging.FileHandler(log_path+"/{:%Y-%m-%d}.log".format(datetime.now()), encoding='utf8')
fileHandler.setFormatter(format)
log.addHandler(fileHandler)

log.setLevel(level=logging.DEBUG)