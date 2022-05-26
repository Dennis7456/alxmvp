from dotenv import load_dotenv
from os import environ

#Load Environment Varriables
load_dotenv('.flaskenv')

class Config:
    # Get the environment variables from .flaskenv
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    #Mail
    MAIL_PORT = environ.get('MAIL_PORT')
    MAIL_USE_TLS = environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_APP_PASSWORD = environ.get('MAIL_APP_PASSWORD')
    MAIL_SENDER_NAME = environ.get('MAIL_SENDER_NAME')