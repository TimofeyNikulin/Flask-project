from app import app
from flask import render_template, redirect
from ..data import db_session
from ..data.users import User
from flask_login import login_user
from requests import get


@app.route('/')
def index():
    return render_template("index.html", title="Главная", get=get)


@app.route('/who_is_a_counselor')
def who_is_a_counselor():
    return render_template("index/who_is_a_counselor.html", title="Кто такой вожатый?", get=get)


@app.route('/what_does_a_counselor_do')
def what_does_a_counselor_do():
    return render_template("index/what_does_a_counselor_do.html", title="Чем занимается вожатый?", get=get)


@app.route('/who_can_become_a_counselor')
def who_can_become_a_counselor():
    return render_template("index/who_can_become_a_counselor.html", title="Кто может стать вожатым?", get=get)
