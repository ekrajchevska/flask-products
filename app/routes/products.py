from flask import request, jsonify
from flask import current_app as app
from flask.wrappers import Response
from app.models import *
from app.services import *
from app import auth
from app.exceptions import *


product_service = ProductService()

# http://localhost:8081/products-api


@app.route("/hello", methods=["GET"])
def hello():
    return {"hello": "world"}


@app.route("/create", methods=["POST"])
@auth.token_required
def create():

    try:
        product_dto = ProductDTO(
            request.json["name"],
            request.json["description"],
            request.json["price"],
            request.json["quantity"],
        )  # request.get_json ?
        new_product = product_service.create_product(product_dto)

    except (KeyError):
        raise InvalidAPIUsage(
            "Invalid product creation. Please specify all fields.", 400
        )

    return new_product


@app.route("/products", methods=["GET"])
def get_products():
    result = product_service.get_all_products()
    return result


@app.route("/product/<int:id>", methods=["GET"])
def get_product_by_id(id: int):
    product = product_service.get_product_by_id(id)
    return product


@app.route("/product/<int:id>", methods=["PUT"])
@auth.token_required
def update_product(id: int):

    data = request.get_json()
    name = description = price = quantity = None
    if "name" in data:
        name = request.json["name"]
    if "description" in data:
        description = request.json["description"]
    if "price" in data:
        price = request.json["price"]
    if "quantity" in data:
        quantity = request.json["quantity"]

    product_dto = ProductDTO(name, description, price, quantity)
    try:
        updated = product_service.update_product(id, product_dto)
    except ProductNotFoundException as e:
        raise InvalidAPIUsage(e.message, e.status_code)

    return updated


@app.route("/product/<int:id>", methods=["DELETE"])
@auth.token_required
def delete_product(id: int):
    try:
        del_product = product_service.delete_product(id)
    except ProductNotFoundException as e:
        raise InvalidAPIUsage(e.message, e.status_code)

    return del_product


@app.route("/buy-products", methods=["POST"])
@auth.token_required
def buy_products():
    bucket = list(request.get_json())
    try:
        product_service.buy_products(bucket)

    except (ProductNotFoundException, InvalidQuantityException) as e:
        raise InvalidAPIUsage(e.message, e.status_code)

    return Response(status=200)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code
