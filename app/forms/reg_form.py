from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, DataRequired


class RegForm(FlaskForm):
    name = StringField(label="Имя:", name="name", id="name", validators=[InputRequired()])
    surname = StringField(label="Фамилия:", name="surname", id="surname", validators=[InputRequired()])
    email = EmailField(label="Почта:", name="email", id="email", validators=[InputRequired()])
    password = PasswordField(label="Пароль:", name="password", id="password", validators=[InputRequired()])