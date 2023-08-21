import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21165589")

API_HASH = os.environ.get("API_HASH", "8cc762f4873e84a7cf0cbfd66a07244b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6458881761:AAGpnLADPVGuRiUqiJOR6Bjb393Cpr2YmJs") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001681552767") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://1234:0000@cluster0.sc33vq5.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))
START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIin in os.environ.get('ADMIN', '2048030675').split()]

PORT = os.environ.get("PORT", "8080")
