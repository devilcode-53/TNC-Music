import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ------------------------------
# Pyrogram API
# ------------------------------
API_ID = int(getenv("API_ID", "22657083"))
API_HASH = getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")
BOT_TOKEN = getenv("BOT_TOKEN", "")

# ------------------------------
# Bot & Owner Info
# ------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME", "OnForHer")
BOT_USERNAME = getenv("BOT_USERNAME", "MahiruProBot")
BOT_NAME = getenv("BOT_NAME", "˹ɱ𝛂ʜ𝛊ʀʊ ɱʊ𝛅𝛊ς˼ ♪ [ 𝛈 ꪮ ⋏∂𝛅 ]")
ASSUSERNAME = getenv("ASSUSERNAME", "MahiruxAssistant")

# ------------------------------
# MongoDB
# ------------------------------
MONGO_DB_URI = getenv(
    "MONGO_DB_URI",
    "mongodb+srv://pikachuxivan_db_user:pikachuxivan@cluster0.9c3hko7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# ------------------------------
# Limits
# ------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
DURATION_LIMIT = DURATION_LIMIT_MIN * 60  # seconds

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# ------------------------------
# IDs (Heroku-safe)
# ------------------------------
def get_int_env(var_name, default):
    value = getenv(var_name, str(default))
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"[ERROR] {var_name} must be a numeric Telegram ID. Got: {value}")

LOGGER_ID = int(getenv("LOGGER_ID", "-1003128590255"))
OWNER_ID = int(getenv("OWNER_ID","7804917014"))

# ------------------------------
# Heroku / Git
# ------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/sexyxcoders/SapnaMusic"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# ------------------------------
# Support links
# ------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/HamsterUpdatess")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+w9ODyFLtrN45YTY1")

for name, link in [("SUPPORT_CHANNEL", SUPPORT_CHANNEL), ("SUPPORT_CHAT", SUPPORT_CHAT)]:
    if link and not re.match(r"(?:http|https)://", link):
        raise SystemExit(f"[ERROR] {name} url is wrong. Must start with https://")

# ------------------------------
# Auto-leaving Assistant
# ------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True") == "True"
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

# ------------------------------
# Song download limits
# ------------------------------
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# ------------------------------
# Spotify
# ------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# ------------------------------
# Sessions
# ------------------------------
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------
# Images
# ------------------------------
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/exw839.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/ddkc5f.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/2nw6zu.jpg"
STATS_IMG_URL = "https://files.catbox.moe/3v8uls.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/1bu0q0.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/1bu0q0.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/1bu0q0.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/1bu0q0.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/1bu0q0.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/dkn1xh.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/dkn1xh.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/dkn1xh.jpg"
