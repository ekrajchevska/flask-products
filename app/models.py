from app import db
from app import ma
from dataclasses import dataclass


product_categories = db.Table('product_categories', 
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    categories = db.relationship('Category', secondary=product_categories, lazy='subquery', 
     backref=db.backref('products', lazy=True))

    def __init__(self, name, description, price, quantity):     # ++
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ProductSchema(ma.Schema):
    class Meta:         # here we define which attr. we want to be visible (ex. if we want to hide the id, we won't include it here)
        fields = ('id', 'name', 'description', 'price', 'quantity')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


@dataclass
class ProductDTO:
    name : str
    description : str
    price : float
    quantity : int