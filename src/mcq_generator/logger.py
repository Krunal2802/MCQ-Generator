import logging
import os
from datetime import datetime

LOG_FILE = "{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # defined structure of name of logfile

log_path = os.path.join(os.getcwd(),"logs") # give a path to a logs folder

os.makedirs(log_path,exist_ok=True) # create a logs folder if not exists

LOG_FILEPATH = os.path.join(log_path, LOG_FILE) # give a path to logfile

logging.basicConfig( # what info should be shown in the logfile
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)