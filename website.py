from flask import Flask,render_template,request,flash,redirect,url_for,session
import config
from models import User,Product
from exts import db
from decorators import login_required


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')

        user = User.query.filter(User.telephone == telephone,User.password==password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            flash('错误的用户名或密码！')
            return redirect(url_for('login'))


@app.route('/regist',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.telephone == telephone).first()
        if user:
            flash('该手机号码已注册！')
            return redirect(url_for('regist'))
        elif password1 != password2:
            flash('两次输入密码不同！')
            return redirect(url_for('regist'))
        else:
            user = User(telephone=telephone,username=username,password=password1)
            db.session.add(user)
            db.session.commit()
            flash('注册成功！')
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    flash('已退出登录！')
    return redirect(url_for('login'))

@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id==user_id).first()
        if user:
            return {'user':user}
    return {}

@app.route('/upload_product',methods=['GET','POST'])
@login_required
def upload_product():
    if request.method == 'GET':
        return render_template('upload_product.html')
    else:
        productname = request.form.get('productname')
        link = request.form.get('link')
        about = request.form.get('about')
        about = '暂无描述' if about=='' else about
        product = Product(productname=productname,link=link,about=about)

        user_id = session.get('user_id')
        user = User.query.filter(User.id==user_id).first()
        product.uploader = user
        db.session.add(product)
        db.session.commit()
        flash('上传商品成功！')
        return redirect(url_for('show_product'))

@app.route('/show_product',methods=['GET','POST'])
@login_required
def show_product():
    context = {
        'products' : Product.query.order_by(Product.create_time.desc()).all()
    }
    return render_template('show_product.html',**context)

@app.route('/show_product_page',methods=['GET','POST'])
@login_required
def show_product_page():
    context = {
        'products' : Product.query.order_by(Product.create_time.desc()).all()
    }
    return render_template('show_product_page.html',**context)

if __name__ == '__main__':
    app.run(host='0.0.0.0')