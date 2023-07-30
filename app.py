from flask import Flask
from models.models import db
from flask_migrate import Migrate
from blueprints.tasks import tasks_blueprint
from blueprints.categories import categories_blueprint
from dotenv import load_dotenv
import os

load_dotenv()

def init_app():
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = os.getenv('DATABASE_URL')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['DEBUG'] = os.getenv('DEBUG')
    app.url_map.strict_slashes = False
    db.init_app(app)
    app.register_blueprint(tasks_blueprint, url_prefix="/api/")
    app.register_blueprint(categories_blueprint, url_prefix="/api/")
    return app


app = init_app()
migrate = Migrate(app, db)
