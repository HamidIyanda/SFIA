from application import db
from application import login_manager
from flask_login import UserMixin
from datetime  import datetime

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False, unique=True)
	content = db.Column(db.String(1000), nullable=False, unique=True)
	date_posted =db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
                return ' '.join([
                        'UserID: ', str (self.id), '\r\n', 'Email: ', self.email,
                        'Title: ', self.title, '\r\n', self.content
                ])


@login_manager.user_loader
def load_user(id):
        return Users.query.get(int(id))

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(150), nullable=False, unique=True)
	first_name = db.Column(db.String(150), nullable=False)
	last_name = db.Column(db.String(150), nullable=False)
	password = db.Column(db.String(200), nullable=False)
	posts = db.relationship('Posts', backref='author', lazy=True)

	def __repr__(self):
                return ''.join([
                        'User: ',self.first_name, ' ' , self.last_name, '\r\n',
                        'Tile: ',self.title, '\r\n', self.content,
                        'Name: ', self.first_name, ' ', self.last_name
                        ])
