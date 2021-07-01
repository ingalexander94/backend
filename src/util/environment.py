import os
from dotenv import load_dotenv

load_dotenv()
SECRET_JWT = os.getenv("SECRET_JWT")
PORT = os.getenv("PORT")
MONGO_URL = os.getenv("MONGO_URL")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
GMAIL_EMAIL = os.getenv("GMAIL_EMAIL")