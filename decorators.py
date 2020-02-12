from functools import wraps
from flask import session,redirect,url_for,flash

def login_required(func):
    
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            flash('请登录后查看')
            return redirect(url_for('login'))

    return wrapper