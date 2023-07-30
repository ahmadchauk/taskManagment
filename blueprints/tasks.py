from models.models import db
from models.models import Task
from flask import Blueprint, request
from controller.taskcontroller import (
    get_all_tasks,
    create_task,
    update_task,
    delete_task,
)
from flask import jsonify

tasks_blueprint = Blueprint("tasks_blueprint", __name__)


@tasks_blueprint.route("/tasks/<id>/", methods=["GET", "PUT", "DELETE"])
def manageTask(id):
    task = Task.query.get(id)
    if task is None:
        return jsonify({"status": False, "msg": "Task not found"}), 404

    if request.method == "GET":
        return jsonify(task.serialize())

    if request.method == "PUT":
        body = request.get_json()
        title = body.get("title")
        description = body.get("description")
        completed = body.get("completed")
        if not title or not description or not completed:
            return jsonify({"Status": False, "msg": "missing fields"})
        if (
            not isinstance(title, str)
            or not isinstance(description, str)
            or not isinstance(completed, bool)
        ):
            return jsonify({"status": False, "msg": "invalid json request"})
        update_task(db, task, body)
        return jsonify({"status": True, "msg": "Task updated successfuly"})

    if request.method == "DELETE":
        delete_task(db, task)
        return jsonify({"status": True, "msg": "Task deleted successfuly"})


@tasks_blueprint.route("/tasks/", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        tasks = get_all_tasks()
        if isinstance(tasks, Task):
            return jsonify(tasks.serialize())
        return jsonify([task.serialize() for task in tasks])

    if request.method == "POST":
        body = request.get_json()
        title = body.get("title")
        description = body.get("description")

        if not title or description:
            return jsonify({"status": False, "msg": "missing fields"})
        if not isinstance(title, str) or not isinstance(description, str):
            return jsonify({"status": False, "msg": "invalid json request"})

        task = create_task(db, title, description)

        return jsonify(task.serialize()), 201
