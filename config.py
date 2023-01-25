from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "25847347"))
API_HASH = getenv("API_HASH", "11569826ebbc9f8b14c3ab1c5ddb937b")

BOT_TOKEN = getenv("BOT_TOKEN", "5907777474:AAELGNY2Dvau5Fn1RuKUjfQw7g9y0motfOg")
OWNER_ID = int(getenv("OWNER_ID", "1327762724"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Aditgbot:0987@cluster0.wutyhoa.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "-1001682109318")
