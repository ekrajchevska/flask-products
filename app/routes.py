from flask import request
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
    name = request.json['name']     # da pobaram dali ima nekoj mehanizam za direktno da se zeme objektot (ProductDTO object)
    description = request.json['description']   # bez manuelno mapiranje
    price = request.json['price']
    quantity = request.json['quantity']

    product_dict = {"name": name, "description": description, "price" : price, "quantity" : quantity}
    new_product = product_service.create_product(product_dict)

    return new_product


@app.route('/products', methods=['GET'])
def get_products():

    result = product_service.get_all_products()
    return result


@app.route('/product/<int:id>', methods=['GET'])
def get_product_by_id(id):
    product = product_service.get_product_by_id(id)

    return product


@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    name = request.json['name']     # ista zabeleska
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    product_dict = {'name' : name, 'description' : description, 'price' : price, 'quantity' : quantity}

    updated = product_service.update_product(id, product_dict)
    
    return updated


@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    del_product = product_service.delete_product(id)
    
    return del_product