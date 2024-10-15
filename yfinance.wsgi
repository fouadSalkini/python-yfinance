import sys
import logging

# Add your project folder to the system path
sys.path.insert(0, "/var/www/html/yfinance_project")

from main import app as application  # Assuming 'app' is your Flask instance