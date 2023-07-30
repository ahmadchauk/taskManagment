from models.models import db, Task
from flask import Blueprint, request, jsonify
from datetime import datetime
from controller.taskController import (
    get_all_tasks,
    create_task,
    update_task,
    delete_task,
)

tasks_blueprint = Blueprint("tasks_blueprint", __name__)

priorities = ["high", "medium", "low"]

current_date = datetime.now().date()

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
        category_id = body.get("category_id")
        priority = body.get("priority")
        due_date = body.get("due_date")
        if (
            not title
            or not description
            or not completed
            or not category_id
            or not priority
            or not due_date
        ):
            return jsonify({"Status": False, "msg": "missing fields"})
        if (
            not isinstance(title, str)
            or not isinstance(description, str)
            or not isinstance(priority, str)
            or not isinstance(completed, bool)
            or not isinstance(category_id, int)
        ):
            return jsonify({"status": False, "msg": "invalid json request"})

        if priority.lower() not in priorities:
            return jsonify(
                {
                    "status": False,
                    "msg": "please choose a priority from this list [high , medium , low]",
                }
            )

        if(datetime.strptime(due_date, "%Y-%m-%d").date() < current_date):
            return jsonify({"status" : False , "msg" : "due date choosed is lower than today"})
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
        category_id = body.get("category_id")
        priority = body.get("priority")
        due_date = body.get("due_date")

        if (
            not title
            or not description
            or not category_id
            or not priority
            or not due_date
        ):
            return jsonify({"status": False, "msg": "missing fields"})

        if (
            not isinstance(title, str)
            or not isinstance(description, str)
            or not isinstance(category_id, int)
            or not isinstance(priority, str)
        ):
            return jsonify({"status": False, "msg": "invalid json request"})

        if priority.lower() not in priorities:
            return jsonify(
                {
                    "status": False,
                    "msg": "please choose a priority from this list [high , medium , low]",
                }
            )
        
        if(datetime.strptime(due_date, "%Y-%m-%d").date() < current_date):
            return jsonify({"status" : False , "msg" : "due date choosed is lower than today"})

        task = create_task(
            db, title, category_id, priority.upper(), due_date, description
        )

        return jsonify(task.serialize()), 201
