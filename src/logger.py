import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True)   ## It make folder with name of "log"

LOG_FILE = os.path.join(LOGS_DIR,f"log_{datetime.now().strftime('%Y-%m-%d')}.log")   ## Out file name format look like: "log_2025_07_24.log".

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,   ### There are three layer: info, warning and error.
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    return logger













