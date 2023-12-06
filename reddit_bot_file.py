import praw
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
client_id = os.getenv("WEB_APP_STRING")
client_secret = os.getenv("REDDIT_SECRET_STRING")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
user_agent = os.getenv("APP_NAME")
