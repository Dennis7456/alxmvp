import os
# from dotenv import load_dotenv
# from pathlib import Path

# env_path = Path('../') / '.env'
# load_dotenv(dotenv_path=env_path)
class Config:
    #Env
    SECRET_KEY = os.getenv('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    uri = os.getenv('DATABASE_URL')
    if uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    # rest of connection code using the connection string `uri`
    SQLALCHEMY_DATABASE_URI = uri

    #Mail
    #MAIL_SERVER = 'smtp.gmail.com'
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')