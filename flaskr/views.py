#views.py
from flask import request,render_template,redirect,url_for,flash,Blueprint
from flaskr import db
from flaskr.forms import RegisterDrink,DeleteDrink
from flaskr.models import DrinkList

@app.route('/drink_list')
def drink_list():
    drinks = DrinkList.query.all()
    delete_form = DeleteDrink(request.form)
    return render_template('drink_list.html',delete_form=delete_form,drinks=drinks)

@app.route('/add_drink',methods=['GET','POST'])
def add_drink():
    form = RegisterDrink(request.form)
    if request.method=='POST' and form.validate():
        for regist in range(form.quantity.data):
            productName=form.productName.data
            jancode=''
            with db.session.begin(subtransactions=True):
                new_drink = DrinkList(productName,jancode)
                db.session.add(new_drink)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_drink.html',form=form)

@app.route('/delete_drink',methods=['GET','POST'])
def delete_drink():
    form = DeleteDrink(request.form)
    if request.method=='POST' and form.validate():
        with db.session.begin(subtransactions=True):
            id=form.id.data
            drink=DrinkList.query.get(id)
            db.session.delete(drink)
        db.session.commit()
        return redirect(url_for('home'))
    return redirect(url_for('home'))