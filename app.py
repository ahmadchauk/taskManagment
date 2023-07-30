from flask import Flask
from models.models import db
from flask_migrate import Migrate
from blueprints.tasks import tasks_blueprint


def create_app():
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:12345678@localhost:5432/tasks_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.url_map.strict_slashes = False
    db.init_app(app)
    app.register_blueprint(tasks_blueprint, url_prefix="/api/")
    return app


app = create_app()
migrate = Migrate(app, db)
