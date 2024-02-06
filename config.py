import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "29500042"))
API_HASH = environ.get("API_HASH", "a8347fcbfff3351477c86f2383b04d4b")
BOT_TOKEN = environ.get("BOT_TOKEN", "6865747183:AAGZ4XHgKkAbk1fT357XoHmVtsnwnQc3Rrc")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "1002138009666"))
ADMINS = int(environ.get("ADMINS", "1117977884,6815505574,5772329729"))
DB_URI = environ.get("DB_URI", "mongodb+srv://Aniket07:Aniket07@aniket.mjotyuh.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "Anichatgptbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
