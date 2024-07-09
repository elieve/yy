import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv(".env")


API_ID = int(getenv("API_ID", "20773506")) #optional
API_HASH = getenv("API_HASH", "4ff20535621ee6f9aa6ba9443b0ec592") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID", "5862907188"))
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "").split()))


ADMIN1_ID.append(5862907188)
ADMIN2_ID.append(5862907188)


MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Bayu:bayu@bayu.2donbau.mongodb.net/?retryWrites=true&w=majority&appName=bayu")
BOT_TOKEN = getenv("BOT_TOKEN", "7003599470:AAHHlC_NRrcTYx-Fci5Q3-hgsW-tW3avIvA")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "False"))
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT", "AKU TERKENTOD MAS")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "-1002169998808").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "naya") #don't change
REPO_URL = getenv("REPO_URL", "https://github.com/elieve/yy")
CMD_HNDLR = getenv("CMD_HNDLR", ",")
SUPPORT = int(getenv("SUPPORT", "-1002169998808"))
CHANNEL = int(getenv("CHANNEL", "-1002169998808"))
SESSION1 = getenv("SESSION1", "BQE8-oIAcP-I6Byn32OFKbg9UztjroulSqYc1H_DnfiPp0Hzs1eM-0Io4tsHXeldTL6pvsC4eZHHukXo0R9t8pOzx-NqZM8Pbqn6fhpvRKUzeplyd56UOmm3qnMsSbLgGTVEclBokNPyaW_qwfR-Lrykpk2ZlO97khDn_t7O4fors2iJaEit_v-9OJIsYJYNKhg-eJ1FX_A1z_yMMdMp0Ird8jsZTdGeE-m0cKVvuAPv84qk_M1NoCpF-CzW9kKcOehRLBuMGXqVqcTGhD3lbsC2vF3jUkdSbD4RWoXTf3jRCnckxPS0WBLKw2z5D_gFgcLlI48y2GWDVkP_a2tWGX2ZOYgObwAAAAFddN00AA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13 = getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
SESSION21 = getenv("SESSION21", "")
SESSION22 = getenv("SESSION22", "")
SESSION23 = getenv("SESSION23", "")
SESSION24 = getenv("SESSION24", "")
SESSION25 = getenv("SESSION25", "")
SESSION26 = getenv("SESSION26", "")
SESSION27 = getenv("SESSION27", "")
SESSION28 = getenv("SESSION28", "")
SESSION29 = getenv("SESSION29", "")
SESSION30 = getenv("SESSION30", "")
SESSION31 = getenv("SESSION31", "")
SESSION32 = getenv("SESSION32", "")
SESSION33 = getenv("SESSION33", "")
SESSION34 = getenv("SESSION34", "")
SESSION35 = getenv("SESSION35", "")
