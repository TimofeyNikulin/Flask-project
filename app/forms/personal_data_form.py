from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, IntegerField, DateField
from wtforms.validators import InputRequired, DataRequired


class PersonalDataForm(FlaskForm):
    name = StringField(label="Имя", name="name", id="name",
                       validators=[InputRequired()])
    surname = StringField(label="Фамилия", name="surname",
                          id="surname", validators=[InputRequired()])
    patronymic = StringField(
        label="Отчество", name="patronymic", id="patronymic")
    phone_number = StringField(
        label="Телефон", name="phone_number", id="phone_number", validators=[InputRequired()])
    date_of_birthday = DateField(
        label="Дата рождения", name="date_of_birthday", id="date_of_birthday", validators=[InputRequired()])
    age = IntegerField(label="Возраст", name="age", id="age",
                       validators=[InputRequired()])
    region = StringField(label="Регион", name="region")
    town = StringField(label="Город", name="town", id="town")
    municip_obraz = StringField(
        label="Муниципальное образование", name="municip_obraz", id="municip_obraz")
    education_organisation = StringField(
        label="Образовательная организация", name="education_organisation", id="education_organisation", validators=[InputRequired()])
