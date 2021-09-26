from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Products(db.Model):
    name = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    weight = db.Column(db.Integer)
    sku = db.Column(db.String(100), primary_key=True)
    available = db.Column(db.Boolean)


INITIAL_DATA = [
    {
    "name": "ABC",
    "brand": "ABC_Brand",
    "weight": 1,
    "sku": "100",
    "available": False
    },
    {
    "name": "DEF",
    "brand": "DEF_Brand",
    "weight": 2,
    "sku": "200",
    "available": False
    },
    {
    "name": "XYZ",
    "brand": "XYZ_Brand",
    "weight": 3,
    "sku": "300",
    "available": False
    }
]


# Delete database file if it exists currently
if os.path.exists('products.db'):
    os.remove('products.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for data in INITIAL_DATA:
    d = Products(name=data['name'], brand=data['brand'], weight=data['weight'], sku=data['sku'], available=data['available'])
    db.session.add(d)

db.session.commit()