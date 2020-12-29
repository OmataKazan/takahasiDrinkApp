#views.py
from flask import request,render_template,redirect,url_for,flash,Blueprint
from flaskr import db,login_manager
from flaskr.forms import RegisterDrink,DeleteDrink,LoginForm,RegisterForm
from flaskr.models import DrinkList,drink_schema,User
from flask_login import login_required,login_user,logout_user

bp = Blueprint('app', __name__, url_prefix='')

#-----ログイン処理設定----#
login_manager.login_view = 'app.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
#-----ログイン処理設定----#
@bp.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.select_by_username(form.username.data)
        if user and user.validate_password(form.password.data):
            login_user(user,remember=True)
            next = request.args.get('next')
            if not next:
                next = url_for('app.drink_list')
            return redirect(next)
    return render_template('login.html',form=form)

#-----ログイン・ログアウト----#

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/drink_list')
@login_required
def drink_list():
    drinks = DrinkList.query.all()
    delete_form = DeleteDrink(request.form)
    return render_template('drink_list.html',delete_form=delete_form,drinks=drinks)

@bp.route('/add_drink',methods=['GET','POST'])
def add_drink():
    form = RegisterDrink(request.form)
    if request.method=='POST' and form.validate():
        for regist in range(form.quantity.data):
            productName=form.drinkname.data
            jancode=''
            with db.session.begin(subtransactions=True):
                new_drink = DrinkList(productName,jancode)
                db.session.add(new_drink)
            db.session.commit()
        return redirect(url_for('app.drink_list'))
    return render_template('add_drink.html',form=form)

@bp.route('/delete_drink',methods=['GET','POST'])
def delete_drink():
    form = DeleteDrink(request.form)
    if request.method=='POST' and form.validate():
        print(form.id.data)
        with db.session.begin(subtransactions=True):
            id=form.id.data
            drink=DrinkList.query.get(id)
            db.session.delete(drink)
        db.session.commit()
        return redirect(url_for('app.drink_list'))
    return redirect(url_for('app.drink_list'))

@bp.route('/api/adddrink',methods=["POST"])
def api_post():
    if not "productName" and not "jancode" in request.json:
      return "error"
    item = DrinkList(productName=request.json["productName"],jancode=request.json["jancode"])
    db.session.add(item)
    db.session.commit()
    return drink_schema.jsonify(item)
    