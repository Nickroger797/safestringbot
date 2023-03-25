from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "22456077"))
API_HASH = getenv("API_HASH", "ac0947297bfd7e83be7e1f311c7c4171")

BOT_TOKEN = getenv("BOT_TOKEN", "5907777474:AAEGO0VwZmmABysTec52usd7RE3jY7Scgd8")
OWNER_ID = int(getenv("OWNER_ID", "1420828558"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Aditgbot:0987@cluster0.wutyhoa.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "nickallbots")
