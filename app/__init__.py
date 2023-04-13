from flask import Flask, render_template
from flask_login import LoginManager
from flask_socketio import SocketIO


app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SECRET_KEY"] = "vogatie_secret_key"
socket = SocketIO(app)
login_manager = LoginManager()
login_manager.init_app(app)


from .data import db_session
from .data.users import User
from .data.messages import Message
from .controllers import user_controller
from .controllers import docs_controller
from .controllers import index_controller


@socket.on('message')
def handlemsg(msg):
    print(type(msg))
    db_sess = db_session.create_session()
    message = Message(user_id=int(msg["user_id"]), text=msg["text"])
    db_sess.add(message)
    db_sess.commit()
    socket.emit('my responce', message.content(), include_self=True)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)
