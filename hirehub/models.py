from datetime import datetime, timedelta
import pytz
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import jwt
from flask import current_app
from hirehub import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    '''Function to generate user token
    N/B: TimedJSONWebSignatureSerializer has been discontinued'''
    # def get_reset_token(self, expires_sec=1800):
    #     # s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    #     # return s.dumps({'user_id': self.id}).decode('utf-8')

    ''' Using pyjwt instead but authlib is also a good candidate for this functionality'''
    def get_reset_token(self, expiration=600):
        without_timezone = datetime.now()
        timezone = pytz.timezone("UTC")
        with_timezone = timezone.localize(without_timezone)
        reset_token = jwt.encode(
           {
               "confirm": self.id,
               "exp": with_timezone
               + timedelta(seconds=expiration)
                       },
                       current_app.config['SECRET_KEY'],
                       algorithm="HS256"
        )
        return reset_token
        '''Function to verify user token'''
    # @staticmethod
    # def verify_reset_token(token):
    #     # s = Serializer(current_app.config['SECRET_KEY'])
    #     # try:
    #     #     user_id = s.loads(token)['user_id']
    #     # except:
    #     #     return None
    #     # return User.query.get(user_id)

    @staticmethod
    def verify_reset_token(token):
        try:
            data = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                leeway=timedelta(seconds=10),
                algorithms=["HS256"]
            )
            user_id = data.get('confirm')
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"