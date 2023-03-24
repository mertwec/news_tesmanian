import os
import logging
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

LOGIN = config.get('user',"LOGIN", fallback='')
PASSWORD = config.get('user',"PASSWORD", fallback='')

BOT_TOKEN = config.get('bot',"BOT_TOKEN", fallback='')
CHAT_ID =  config.get('bot', "CHAT_ID", fallback='')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_URL = "https://www.tesmanian.com"
PARSING_URL = ROOT_URL + "/blogs/tesmanian-blog"
AUTH_URL = ROOT_URL + "/account/login"

JSON_DB_DIR = "data"
JSON_DB = 'news.json'
JSON_PATH = os.path.join(JSON_DB_DIR, JSON_DB)

PERIOD = 15 # sec

logging.basicConfig(
    filename=os.path.join(BASE_DIR, "log_scraping.log"),
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s: %(name)s-%(levelname)s %(message)s",
)

logger = logging.getLogger(name = "info_log")

message = f"""
settings:
\tURL: {PARSING_URL}
\tSAVE_DB: {JSON_PATH}
"""

logger.info(message)
