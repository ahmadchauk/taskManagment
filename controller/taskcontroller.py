from models.models import Task


def get_all_tasks():
    tasks = Task.query.all()
    return tasks


def create_task(db, title,category_id, description):
    task = Task(title, category_id, description)
    db.session.add(task)
    db.session.commit()
    return task


def update_task(db, task, body):
    task.title = body.get("title", task.title)
    task.description = body.get("description", task.description)
    task.completed = body.get("completed", task.completed)
    task.category_id = body.get("category_id", task.category_id)
    db.session.commit()


def delete_task(db, task):
    db.session.delete(task)
    db.session.commit()
