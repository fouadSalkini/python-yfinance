import sys
import logging
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Add your project folder to the system path
sys.path.insert(0, getenv("PROJECT_PATH"))

from main import app as application  # Assuming 'app' is your Flask instance