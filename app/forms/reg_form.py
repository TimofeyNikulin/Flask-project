from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, DataRequired


class RegForm(FlaskForm):
    email = EmailField(label="Почта:", name="email",
                       id="email", validators=[InputRequired()])
    password = PasswordField(
        label="Пароль:", name="password", id="password", validators=[InputRequired()])
