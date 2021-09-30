"""
This is a Flask app to demonstrate REST API for
Product Management System.
We are using SQLAlchemy module for managing the DB.
"""

import json
from flask import request, Response
from product_model import Products, db, app

#status code errors handeling
@app.errorhandler(404)
def handle_404_error(_error):
    """Return a 404 http status code"""
    return Response(json.dumps({'error': 'Not Found'}), 404)

@app.errorhandler(500)
def handle_500_error(_error):
    """Return a 500 http status code"""
    return Response(json.dumps({'error': 'Internal server error occured'}), 500)

@app.errorhandler(400)
def handle_400_error(_error):
    """Return a 400 http status code"""
    return Response(json.dumps({'error': 'Misunderstood or Bad request'}), 400)

@app.errorhandler(401)
def handle_401_error(_error):
    """Return a 401 http status code"""
    return Response(json.dumps({'error': 'Unauthorized'}), 401)

@app.route('/products', methods=['GET', 'POST'])
def api_products():
    """
        GET  /products  returns a JSON response
        POST  /products  returns a JSON response
    """

    if request.method == "GET":
        tasks = Products.query.all()
        all_products = {}
        for task in tasks:
            all_products[task.sku] = {"name": task.name, "brand": task.brand,
            "weight": task.weight, "sku": task.sku, "available": task.available}
        return Response(json.dumps(all_products), status=200, mimetype='application/json')
    elif request.method == "POST":
        req_data = request.get_json()
        sku_id = req_data['sku']
        task = Products.query.filter_by(sku=sku_id).first()
        if task:
            data = {"sku": sku_id, "message": "product "+ sku_id + " already exists"}
            return Response(json.dumps(data), 409)
        product_obj = Products(name=req_data['name'], brand=req_data['brand'],
        weight=req_data['weight'], sku=req_data['sku'], available=req_data['available'])
        db.session.add(product_obj)
        db.session.commit()
        after_commit = Products.query.filter_by(sku=sku_id).first()
        data = {"sku": after_commit.sku, "message": "product "+ after_commit.sku + " created"}
        return Response(json.dumps(data), status=201, mimetype='application/json')

@app.route('/products/<product_id>', methods=['GET', 'DELETE', 'PATCH', 'PUT'])
def api_each_products(product_id):
    """
    GET  /products/<product_id>   returns a JSON response
    PATCH   /products/<product_id>   returns a JSON response
    PUT     /products/<product_id>   returns a JSON response
    DELETE  /products/<product_id>   returns a JSON response
    """
    if request.method == "GET":
        task = Products.query.filter_by(sku=product_id).first()
        if not task:
            return Response("Product Does Not Exist", 404)
        products = {}
        products[product_id] = {"name": task.name, "brand": task.brand,
        "weight": task.weight, "sku": task.sku, "available": task.available}
        return Response(json.dumps(products.get(product_id)), 200)
    elif request.method == "DELETE":
        task = Products.query.filter_by(sku=product_id).first()
        if not task:
            return Response("Product Does Not Exist", 204)
        db.session.delete(task)
        db.session.commit()
        return Response("Product deleted", 200)
    elif request.method == "PATCH":
        req_data = request.get_json()
        task = Products.query.filter_by(sku=product_id).first()
        if not task:
            return Response("Product Does Not Exist", 404)
        if req_data['name']:
            task.name = req_data['name']
        if req_data['brand']:
            task.brand = req_data['brand']
        if req_data['weight']:
            task.weight = req_data['weight']
        if req_data['sku']:
            task.sku = req_data['sku']
        task.available = req_data['available']
        db.session.commit()
        data = {"sku": task.sku, "message": "Product "+ task.sku + " has been updated"}
        return Response(json.dumps(data), 200)
    elif request.method == "PUT":
        req_data = request.get_json()
        task = Products.query.filter_by(sku=product_id).first()
        if not task:
            product_obj = Products(name=req_data['name'], brand=req_data['brand'],
            weight=req_data['weight'], sku=req_data['sku'], available=req_data['available'])
            db.session.add(product_obj)
            db.session.commit()
            after_commit = Products.query.filter_by(sku=product_id).first()
            data = {"sku": after_commit.sku, "message": "product "+ after_commit.sku + " created"}
            return Response(json.dumps(data), status=201, mimetype='application/json')
        if req_data['name']:
            task.name = req_data['name']
        if req_data['brand']:
            task.brand = req_data['brand']
        if req_data['weight']:
            task.weight = req_data['weight']
        if req_data['sku']:
            task.sku = req_data['sku']
        task.available = req_data['available']
        db.session.commit()
        data = {"sku": task.sku, "message": "Product "+ task.sku + " has been updated"}
        return Response(json.dumps(data), 200)

if __name__ == '__main__':
    app.run(debug=True)
