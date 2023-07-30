from flask import Flask, make_response, jsonify
from models.models import db
from flask_migrate import Migrate
from blueprints.tasks import tasks_blueprint
from blueprints.categories import categories_blueprint
from dotenv import load_dotenv
import os

load_dotenv()


def init_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DEBUG"] = os.getenv("DEBUG")
    
    app.url_map.strict_slashes = False

    db.init_app(app)

    app.register_blueprint(tasks_blueprint, url_prefix="/api/")
    app.register_blueprint(categories_blueprint, url_prefix="/api/")

    @app.errorhandler(404)
    def handle_404_error(_error):
        return make_response(jsonify({"error": "not found"}), 404)

    @app.errorhandler(500)
    def handle_500_error(_error):
        return make_response(jsonify({"error": "Internal server error"}), 500)

    @app.errorhandler(405)
    def handle_405_error(_error):
        return make_response(jsonify({"error": "Not allowed"}), 405)

    @app.errorhandler(400)
    def handle_400_error(_error):
        return make_response(jsonify({"error": "Bad Request Exceprion"}), 400)

    return app


app = init_app()
migrate = Migrate(app, db)
