from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class TimestampMixin:
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Category(TimestampMixin, db.Model):
    # __tablename__ = "categories"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    tasks = db.relationship("Task", backref="category", lazy=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Category: title: {}>".format(self.title)

    def serialize(self):
        return {"id": self.id, "title": self.title}


class Task(TimestampMixin, db.Model):
    # __tablename__ = "tasks"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)


    def __init__(self, title, category_id, description=None):
        self.title = title
        self.description = description
        self.category_id = category_id

    def __repr__(self):
        return "<Task: title: {} description: {} completed: {}>".format(
            self.title, self.description, self.completed
        )

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "category" : self.category.title
        }
