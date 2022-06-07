import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)
class Config:
    #Env
    FLASK_APP = 'run.app'
    # SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_KEY = '5250d32206145b683d54a6b9795526b8'
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    print(SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    #Mail
    #MAIL_SERVER = 'smtp.gmail.com'
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')