
from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from hirehub.config import Config
from dotenv import load_dotenv



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    #App configurations
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    from hirehub.main.routes import main
    from hirehub.users.routes import users
    from hirehub.jobposts.routes import job_posts
    from hirehub.applications.routes import applications
    from hirehub.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(job_posts)
    app.register_blueprint(applications)
    app.register_blueprint(errors)

    return app