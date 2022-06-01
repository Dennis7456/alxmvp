import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)
class Config:
    #Env
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    #Mail
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_APP_PASSWORD = os.getenv('MAIL_APP_PASSWORD')
    MAIL_SENDER_NAME = os.getenv('MAIL_SENDER_NAME')