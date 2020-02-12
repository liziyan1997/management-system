from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    telephone = db.Column(db.String(11),nullable=False)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    
class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    productname = db.Column(db.String(100),nullable=False)
    link = db.Column(db.String(300),nullable=False)
    about = db.Column(db.String(500))
    create_time = db.Column(db.DateTime,default=datetime.now)
    uploader_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    uploader = db.relationship('User',backref=db.backref('products'))

     