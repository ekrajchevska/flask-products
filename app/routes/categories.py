from flask import request, jsonify
from flask.wrappers import Response
from flask import current_app as app
from app.exceptions import *
from app import auth
from app.services import *


category_service = CategoryService()
product_service = ProductService()


@app.route("/category", methods=["POST"])
@auth.token_required
def create_category():
    try:
        name = request.json["name"]
        new_category = category_service.new_category(name)

    except (KeyError):
        raise InvalidAPIUsage(
            "Invalid category creation. Please specify all fields.", 400
        )

    return new_category


@app.route("/categories", methods=["GET"])
def get_categories():
    categories = category_service.get_all_categories()
    return categories


@app.route("/product-categories", methods=["PUT"])
@auth.token_required
def add_categories_to_products():
    product_id = request.json["product_id"]
    categories_ids = request.json["categories_id"]
    product_service.add_categories(product_id, categories_ids)

    return Response(status=200)
