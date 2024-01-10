import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    patronymic = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phone_number = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    date_of_birthday = sqlalchemy.Column(sqlalchemy.Date, nullable=False)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    region = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    town = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    municip_obraz = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    education_organisation = sqlalchemy.Column(
        sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now)
    messages = orm.relationship("Message", back_populates='user')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def get_hashed_password(password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self) -> str:
        return f'USER [ID: {self.id} NAME: {self.name} SURNAME: {self.surname} EMAIL: {self.email}]'
