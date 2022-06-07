from os import environ
# from dotenv import load_dotenv
# from pathlib import Path

# env_path = Path('./') / '.env'
# load_dotenv(dotenv_path=env_path)
# class Config:
#     #Env
#     SECRET_KEY = 'b8245c88c4eb4666124a25702e896f0d'
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
#     TEST=os.getenv('TEST')
#     print(TEST)
#     #Mail
#     MAIL_SERVER = os.getenv('MAIL_SERVER')
#     MAIL_PORT = os.getenv('MAIL_PORT')
#     MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
#     MAIL_USERNAME = os.getenv('MAIL_USERNAME')
#     MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')


SECRET_KEY = environ.get('SECRET_KEY')
uri = environ.get('DATABASE_URL')
if uri.startswith("postgres://"):
    uri = uri.replace('postgres://', 'postgresql://', 1)
    
SQLALCHEMY_DATABASE_URI = uri