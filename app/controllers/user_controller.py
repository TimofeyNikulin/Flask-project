from app import app
from flask import render_template, redirect
from ..data import db_session
from ..forms.reg_form import RegForm
from ..forms.log_form import LogForm
from ..forms.personal_data_form import PersonalDataForm
from ..data.users import User
from ..data.messages import Message
from flask_login import login_user, login_required, logout_user
from requests import get
from flask_socketio import send, emit


email = ''
hashed_password = ''


@app.route('/registrate', methods=["GET", "POST"])
def register():
    global email, hashed_password
    form = RegForm()
    if form.validate_on_submit():
        try:
            email = form.email.data
            hashed_password = User.get_hashed_password(form.password.data)
            return redirect(f'/registrate/set_personal_data')
        except:
            return render_template('reg.html', title='Регистрация', form=form, message="Запись с такой почтой уже существует!")
    return render_template('reg.html', title='Регистрация', form=form, message="", get=get)


@app.route('/registrate/set_personal_data', methods=["GET", "POST"])
def set_personal_data():
    global email, hashed_password
    form = PersonalDataForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        try:
            user = User(
                name=form.name.data,
                email=email,
                surname=form.surname.data,
                patronymic=form.patronymic.data,
                phone_number=form.phone_number.data,
                date_of_birthday=form.date_of_birthday.data,
                age=form.age.data,
                region=form.region.data,
                town=form.town.data,
                municip_obraz=form.municip_obraz.data,
                education_organisation=form.education_organisation.data,
                hashed_password=hashed_password
            )
            email = ''
            hashed_password = ''
            db_sess.add(user)
            db_sess.commit()
            return redirect('/login')
        except:
            return render_template('personal_data.html', title='Ввод персональных данных', form=form, message="Запись с такой почтой уже существует!")
    return render_template('personal_data.html', title='Ввод персональных данных', form=form, message="", get=get)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LogForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               title='Вход',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Вход', form=form, message="", get=get)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
