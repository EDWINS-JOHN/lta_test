
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL", "https://lta.welovetrucks.co/login")
EMAIL = os.getenv("Email", "testlta@gmail.com")
PASSWORD = os.getenv("PASSWORD", "@Lta123")