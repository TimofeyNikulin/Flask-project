import flask

from . import db_session
from .users import User
from .messages import Message

blueprint = flask.Blueprint(
    'data_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/data')
def get_data():
    db_sess = db_session.create_session()
    messages = db_sess.query(Message).all()
    return flask.jsonify(
        {
            'messages':
                [item.to_dict(only=('user_id', 'text')) 
                 for item in messages[::-1]],
            'users': [{item.name: item.id} for item in db_sess.query(User).all()]
        }
    )