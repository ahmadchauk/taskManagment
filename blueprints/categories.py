from models.models import Category, db
from flask import Blueprint, request, jsonify
from controller.categoryController import (
    get_all_categories,
    create_category,
    update_category,
    delete_category,
)

categories_blueprint = Blueprint("categories_blueprint", __name__)


@categories_blueprint.route("/categories/<id>", methods=["GET", "PUT", "DELETE"])
def manageCategory(id):
    category = Category.query.get(id)

    if category is None:
        return jsonify({"status": False, "msg": "Category not found"}), 404
    
    if request.method == "GET":
        return jsonify(category.serialize())
    
    if request.method == "PUT":
        body = request.get_json()
        title = body.get("title")
        if not title:
            return jsonify({"status": False, "msg": "missing fields"})
        if not isinstance(title, str):
            return jsonify({"status": False, "msg": "invalid json"})
        update_category(db, category, body)
        return jsonify({"status": True, "msg": "Category updated successfuly"})

    if request.method == "DELETE":
        delete_category(db, category)
        return jsonify({"status": True, "msg": "Category deleted successfuly"})


@categories_blueprint.route("/categories/", methods=["GET", "POST"])
def categories():
    if request.method == "GET":
        categories = get_all_categories()
        if isinstance(categories, Category):
            return jsonify(categories.serialize())
        return jsonify([category.serialize() for category in categories])
    
    if request.method == "POST":
        body = request.get_json()
        title = body.get("title")
        if not title:
            return jsonify({"status": False, "msg": "missing fields"})
        if not isinstance(title, str):
            return jsonify({"status": False, "msg": "invalid json request"})

        cateory = create_category(db, title)
        return jsonify({"status": True, "msg": "Category inserted successfuly" , "category" : cateory.serialize()}) , 201

        # return jsonify(cateory.serialize()), 201
