from app import app
from flask import render_template, redirect
from ..data import db_session
from ..forms.reg_form import RegForm
from ..forms.log_form import LogForm
from ..data.users import User
from ..data.messages import Message
from flask_login import login_user, login_required, logout_user
from requests import get
from flask_socketio import send, emit


@app.route('/registrate', methods=["GET", "POST"])
def register():
    form = RegForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        try:
            user = User(
                name=form.name.data,
                email=form.email.data,
                surname=form.surname.data
            )
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()
            return redirect('/')
        except:
            return render_template('reg.html', title='Регистрация', form=form, message="Запись с такой почтой уже существует!")
    return render_template('reg.html', title='Регистрация', form=form, message="", get=get)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LogForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Регистрация', form=form, message="", get=get)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")




