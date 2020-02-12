import os

DEBUG = True

SECRET_KEY = os.urandom(24)

DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DATABASE = 'website'
USERNAME = 'root'
PASSWORD = '971211'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,DB_HOST,DB_PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

