from datetime import datetime
from proj import db, login_manager
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
    userquerys = db.relationship('UserQuery', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class UserQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"UserQuery('{self.title}', '{self.date_posted}')"
####okay 
class TwitterUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique = False, nullable = False)
    username = db.Column(db.String(120), unique=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    def __repr__(self):
        return f"TwitterUser('{self.user_id}', '{self.username}')"
###okay 
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique = False, nullable = False)
    tweet = db.Column(db.String(120), unique=False, nullable=False)
    likes_count = db.Column(db.Integer, unique = False)
    replies_count = db.Column(db.Integer, unique = False)
    retweets_count = db.Column(db.Integer, unique = False)
    def __repr__(self):
        return f"Tweet('{self.user_id}', '{self.tweet}')"
    