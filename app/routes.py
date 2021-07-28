import re
from flask import request, jsonify
from flask import current_app as app
from flask.wrappers import Response
from .models import *
from .services import *


product_service = ProductService()

@app.route('/hello', methods=['GET'])
def hello():
    return {'hello' : 'world'}

@app.route('/create', methods=['POST'])
def create():   

    try:
        product_dto = ProductDTO(request.json['name'], request.json['description'], 
        request.json['price'], request.json['quantity'])        # request.get_json ?
        new_product = product_service.create_product(product_dto)

    except (KeyError):
        raise InvalidAPIUsage("Invalid product creation. Please specify all fields.", 400)

    return new_product


@app.route('/products', methods=['GET'])
def get_products():

    result = product_service.get_all_products()
    return result


@app.route('/product/<int:id>', methods=['GET'])
def get_product_by_id(id : int):
    product = product_service.get_product_by_id(id)

    return product


@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id : int):

    data = request.get_json()
    name = description = price = quantity = None
    if 'name' in data:
        name = request.json['name']
    if 'description' in data:
        description = request.json['description']
    if 'price' in data:
        price = request.json['price']
    if 'quantity' in data:
        quantity = request.json['quantity']

    product_dto = ProductDTO(name, description, price, quantity) 
    updated = product_service.update_product(id, product_dto)

    if updated is None:
        raise InvalidAPIUsage("No product with such ID.", 404)
    
    return updated


@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id : int):
    del_product = product_service.delete_product(id)

    if del_product is None:
        raise InvalidAPIUsage("No product with such ID.", 404)
    
    return del_product


@app.route('/buy-products', methods=['POST'])
def buy_products():
    bucket = list(request.get_json())
    code = product_service.buy_products(bucket)
    if code == 404:
        raise InvalidAPIUsage("No product with such ID.", 404)
    elif code == 400:
        raise InvalidAPIUsage("Order exceeds available quantity", 400)
    
    return Response(status=200)



# Exceptions

class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message : str, status_code = None):
        super().__init__()

        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        response = dict()
        response['message'] = self.message
        return response

@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict())
