from models.models import Category


def get_all_categories():
    categories = Category.query.all()
    return categories


def create_category(db, title):
    category = Category(title)
    db.session.add(category)
    db.session.commit()
    return category


def update_category(db, category, body):
    category.title = body.get("title", category.title)
    db.session.commit()


def delete_category(db, category):
    db.session.delete(category)
    db.session.commit()
