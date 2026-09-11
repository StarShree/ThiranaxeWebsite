import os
import sys
from pathlib import Path

# Add project root directory to sys.path so Django can locate portfolio_project and portfolio
BASE_DIR = Path(__file__).resolve().parent.parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Ensure PyMySQL replaces MySQLdb before Django initializes
import pymysql
pymysql.install_as_MySQLdb()

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_project.settings")

# Initialize WSGI application
import serverless_wsgi
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

def handler(event, context):
    """
    AWS Lambda / Netlify Function handler wrapper for Django WSGI application
    """
    return serverless_wsgi.handle_request(application, event, context)
