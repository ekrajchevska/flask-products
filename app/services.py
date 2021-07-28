from .models import *
from app import db

# da ima transactional metod

# da se kreira uste edna tabela kategorija i tagovi (many-to-many so product)
# da moze da se dodade kategorija (edna ili povekje) na produktive 
# ----- isto i so tag
# da razgledam Flask Migrations (kje uspee i so db.create_all da gi kreira ama ne se prai taka :) ) 

# /buy-products i naveduvas (so ime probs) koi produkti gi sakash
# na tie sto se kupuvaat da im se namali quantity 


class ProductService:

    def create_product(self, product : ProductDTO):
        """[summary]

        Args:
            product (dict): [key-value pairs of the product to be added in database]

        Returns:
            obj: [the newly created object in json-format]
        """

        new_product = Product(product.name, product.description, product.price, product.quantity)

        db.session.add(new_product)
        db.session.commit()

        return product_schema.jsonify(new_product)


    def get_all_products(self):
        """[summary]

        Returns:
            [list]: [list of all products in json-format]
        """
        all_products = Product.query.all()
        return products_schema.jsonify(all_products)

    
    def get_product_by_id(self, id : int):
        """[summary]

        Args:
            id (int): [the id of the product to be returned]

        Returns:
            obj: [the product object in json-format]
        """
        
        product = Product.query.get(id)

        return product_schema.jsonify(product)

    
    def update_product(self, id : int, product : ProductDTO):
        """[summary]

        Args:
            id (int): [the id of the product to be updated]

            product (dict): [dict of updated product fields]

        Returns:
            [obj]: [the updated product object in json-format]
        """

        updated_prod = Product.query.get(id)
        if updated_prod is None:
            return None
            
        if product.name is not None:
            updated_prod.name = product.name
        if product.description is not None:
            updated_prod.description = product.description
        if product.price is not None:
            updated_prod.price = product.price
        if product.quantity is not None:
            updated_prod.quantity = product.quantity

        db.session.commit()

        return product_schema.jsonify(updated_prod)


    def delete_product(self, id : int):
        """[summary]

        Args:
            id (int): [the id of the product to be deleted]

        Returns:
            [obj]: [the deleted product object in json-format]
        """
        product = Product.query.get(id)

        if product is None:
            return None
        
        db.session.delete(product)
        db.session.commit()

        return product_schema.jsonify(product)


    def buy_products(self, products : list):
        for product in products:
            updated_prod = Product.query.get(product['id'])

            if updated_prod is None:
                db.session.rollback()
                return 404

            if updated_prod.quantity < product['quantity']:
                db.session.rollback()
                return 400
            updated_prod.quantity -= product['quantity']
            
        db.session.commit()

        return 200
