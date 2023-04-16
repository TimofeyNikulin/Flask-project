from app import app, socket
from app.data import db_session, api
import os


if __name__ == "__main__":
    db_session.global_init("app/db/web.sqlite")
    app.register_blueprint(api.blueprint)
    app.run()