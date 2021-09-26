from flask import Flask, make_response, jsonify, request
from flask_restful import reqparse
from ProductModel import Products
from ProductModel import *



@app.route('/products', methods=['GET', 'POST'])
def api_products():
    if request.method == "GET":
        tasks = Products.query.all()
        all_products = {}
        for task in tasks:
            all_products[task.sku] = {"name": task.name, "brand": task.brand, "weight": task.weight, "sku": task.sku, "available": task.available}
        return make_response(jsonify(all_products), 200)
    elif request.method == "POST":
        req_data = request.get_json()
        print(req_data)
        sku_id = req_data['sku']
        task = Products.query.filter_by(sku=sku_id).first()
        if task:
           data = {"sku": sku_id, "message": "product "+ sku_id + " already exists"}
           return make_response(jsonify(data), 409)
        product_obj = Products(name=req_data['name'], brand=req_data['brand'], weight=req_data['weight'], sku=req_data['sku'], available=req_data['available'])
        db.session.add(product_obj)
        db.session.commit()
        after_commit = Products.query.filter_by(sku=sku_id).first()
        data = {"sku": after_commit.sku, "message": "product "+ after_commit.sku + " created"}
        return make_response(jsonify(data), 200)

@app.route('/products/<product_id>', methods=['GET', 'DELETE', 'PUT'])
def api_each_products(product_id):
    if request.method == "GET":
        task = Products.query.filter_by(sku=product_id).first()
        if not task:
            return make_response("Product Does Not Exist", 404)
        else:
            products = {}
            products[product_id] = {"name": task.name, "brand": task.brand, "weight": task.weight, "sku": task.sku, "available": task.available}
            return make_response(jsonify(products.get(product_id)), 200)
    elif request.method == "DELETE":
        task = Products.query.filter_by(sku=product_id).first()
        if not task:
            return make_response("Product Does Not Exist", 404)
        else:
            db.session.delete(task)
            db.session.commit()
        return make_response("Product deleted", 200)
    elif request.method == "PUT":
        req_data = request.get_json()
        task = Products.query.filter_by(sku=product_id).first()
        if not task:
           return make_response("Product Does Not Exist", 404)
        if req_data['name']:
            task.name = req_data['name']
        if req_data['brand']:
            task.brand = req_data['brand']
        if req_data['weight']:
            task.weight = req_data['weight']
        if req_data['sku']:
            task.sku = req_data['sku']
        if req_data['available']:
            task.available = req_data['available']
        db.session.commit()
        data = {"sku": task.sku, "message": "Product "+ task.sku + " has been updated"}
        return make_response(jsonify(data), 200)


if __name__ == '__main__':
    app.run(debug=True)
 

    