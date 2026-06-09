import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
base_dir=os.path.dirname(os.path.abspath(__file__))
log_dir=os.path.join(base_dir, "logs")
os.makedirs(log_dir, exist_ok=True)

LOG_FILE_PATH=os.path.join(log_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")