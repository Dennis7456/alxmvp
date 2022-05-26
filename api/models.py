from app import db, login

Class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)