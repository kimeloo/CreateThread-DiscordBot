# Set Logger
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s] : [%(name)10s] --- %(message)s")
log_handler = logging.StreamHandler()
log_handler.setFormatter(log_formatter)
log_warning_formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s] : [%(name)10s] --- %(message)s")
log_warning_handler = logging.FileHandler("event.log")
log_warning_handler.setLevel(logging.INFO)
log_warning_handler.setFormatter(log_warning_formatter)
logger.addHandler(log_handler)
logger.addHandler(log_warning_handler)

# Start Log
logger.info("")
logger.info("Running main.py")
logger.info("")

from discord_automation import config
TOKEN = config.Config().token
config.Config().token = 0