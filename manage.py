from flask_migrate import Migrate
from models.models import db
from app import app


migrate = Migrate(app , db)

