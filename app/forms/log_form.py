from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, BooleanField
from wtforms.validators import InputRequired


class LogForm(FlaskForm):
    email = EmailField(label="Почта:", name="email",
                       id="email", validators=[InputRequired()])
    password = PasswordField(
        label="Пароль:", name="password", id="password", validators=[InputRequired()])
