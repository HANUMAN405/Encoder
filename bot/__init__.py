import os
import logging
import asyncio
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from dotenv import load_dotenv

LOG_FILE_NAME = "Hanu@Log.txt"

if os.path.exists(LOG_FILE_NAME):
    with open(LOG_FILE_NAME, "r+") as f_d:
        f_d.truncate(0)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=2097152000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
LOGS = logging.getLogger(__name__)


THUMB = "https://telegra.ph/file/9fba75d040c1e94950081.jpg"
os.system(f"wget {THUMB} -O thumb.jpg")
ffmpeg = []
ffmpeg.append("-map 0 -c:v libx265 -crf 24 -c:s copy  -s 1280x720 -preset veryfast -c:a libopus -ab 60k -vbr 2 -ac 2 -level 2.1")
try:
 api_id = 19692872  # Replace with your actual API ID
 api_hash = "803249b1faaf2dcd4871d6b9eb46c614"
 bot_token = "5092787930:AAGe5x5sEevHvjrS1ODtVgv1Xr5OYfYi9KY"
 DATABASE_URL = os.environ.get("DATABASE_URL") 
 BOT_USERNAME = "Bhrao_Amazing_Compressor_bot"
 MAX_MESSAGE_LENGTH = 4096
 download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")

# Add your SUDO user IDs directly
 sudo_users = list(set([
    1359873570, 7503742541 # Add more if needed
 ]))

 LOG_CHANNEL = -1001885893314  # Replace with your actual log channel ID
except Exception as e:
 LOGS.info("ENV Are Missing")

app = Client("HaNu", api_id=api_id, api_hash=api_hash, bot_token=bot_token, workers=2)
0
data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
