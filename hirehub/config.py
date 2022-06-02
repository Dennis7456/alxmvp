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
    #MAIL_SERVER = 'smtp.gmail.com'
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    print(f'This is mail server:', MAIL_SERVER)
    print(f'This is mail port:', MAIL_PORT)
    print(f'This is mail TLS:', MAIL_USE_TLS)
    print(f'This is mail username:', MAIL_USERNAME)
    print(f'This is mail password:', MAIL_PASSWORD)