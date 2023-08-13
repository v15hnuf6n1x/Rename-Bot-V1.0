import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21165589")

API_HASH = os.environ.get("API_HASH", "8cc762f4873e84a7cf0cbfd66a07244b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6124452949:AAEga4V0osEmvGQC3VyH26cGYfSmeUoIKpY") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001681552767") 

DB_NAME = os.environ.get("DB_NAME","cluster1")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Erogire:erogirelad@cluster1.boyfnr5.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2048030675').split()]

PORT = os.environ.get("PORT", "8080")
