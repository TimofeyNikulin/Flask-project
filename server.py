from app import app, socket
from app.data import db_session, api


def create_app():
    db_session.global_init("app/db/web.sqlite")
    app.register_blueprint(api.blueprint)
    socket.run(app, host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    create_app()