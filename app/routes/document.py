from flask import request
from flask.wrappers import Response
from flask import current_app as app
from marshmallow.fields import String
from app.auth import token_required
from app.exceptions import *
from app.services import *
from bson import json_util
import json


product_service = ProductService()


@app.route("/document/create", methods=["POST"])
@token_required
def create_product_document():

    try:
        product_dto = ProductDTO(
            request.json["name"],
            request.json["description"],
            request.json["price"],
            request.json["quantity"],
        )  # request.get_json ?

        product_service.create_product_doc(request.json)

    except (KeyError):
        raise InvalidAPIUsage(
            "Invalid product creation. Please specify all fields.", 400
        )
    return Response(status=201)


@app.route("/document/products", methods=["GET"])
def get_products_document():
    result = product_service.get_all_docs()
    data = {
        "data": [
            {
                "name": entry["name"],
                "description": entry["description"],
                "price": entry["price"],
                "quantity": entry["quantity"],
            }
            for entry in result
        ]
    }

    return json.loads(json_util.dumps(data))


@app.route("/document/product/{id}", methods=["GET"])
def get_doc_by_id(id: String):
    obj_id = ObjectId(id)
    prod = product_service.get_product_doc_by_id(obj_id)
    return json.loads(json_util.dumps(prod))


@app.route("/document/product", methods=["PUT"])
@token_required
def update_product_document():
    product_service.update_product_doc(request.json)
    return Response(status=202)


@app.route("/document/product", methods=["DELETE"])
@token_required
def delete_product_document():
    product_service.delete_product_doc(request.json)
    return Response(status=202)
