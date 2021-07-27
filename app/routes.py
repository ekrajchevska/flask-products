from flask import request, jsonify
from flask import current_app as app
from .models import *
from .services import *


# EXCEPTION HANDLING (tuka catch), so klasi obvsly

product_service = ProductService()

@app.route('/hello', methods=['GET'])
def hello():
    return {'hello' : 'world'}

@app.route('/create', methods=['POST'])
def create():   # (product : ProductDTO)

    try:
        name = request.json['name']     # da pobaram dali ima nekoj mehanizam za direktno da se zeme objektot (ProductDTO object)
        description = request.json['description']   # bez manuelno mapiranje
        price = request.json['price']
        quantity = request.json['quantity']

    except (KeyError):
        raise InvalidAPIUsage("Invalid product creation. Please specify all fields.", 400)

    product_dict = {"name": name, "description": description, "price" : price, "quantity" : quantity}
    new_product = product_service.create_product(product_dict)

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

    try:
        name = request.json['name']     # ista zabeleska
        description = request.json['description']
        price = request.json['price']
        quantity = request.json['quantity']

    except (KeyError):
        raise InvalidAPIUsage("Please specify all attributes.", 400)

    product_dict = {'name' : name, 'description' : description, 'price' : price, 'quantity' : quantity}

    updated = product_service.update_product(id, product_dict)

    if updated is None:
        raise InvalidAPIUsage("No product with such ID.", 404)
    
    return updated


@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id : int):
    del_product = product_service.delete_product(id)

    if del_product is None:
        raise InvalidAPIUsage("No product with such ID.", 404)
    
    return del_product



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