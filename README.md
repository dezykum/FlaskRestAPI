# FlaskRestAPI
> In this project, I have worked with Flask to create REST API for all CRUD operations for Product Management System. 
> I have used SQLAlchemy module for managing the DB.

## Steps to run this project:

> Download the project, unzip it, go to the folder path in command prompt.

# Install dependencies using pip
$ pip install -r requirements.txt

# To run the app with database, run the ProductsRestApi.py file
$ python products_restapi.py

# A server will be opened on port 5000. (http://localhost:5000)

### Endpoints
* GET     /products
* GET     /products/:id
* POST    /products
* PATCH   /products/:id
* PUT     /products/:id
* DELETE  /products/:id

### Request Body
``` bash
{
   "name": "LMN", 
   "brand": "LMN_Brand",
   "sku": "155",
   "weight": 10
   "available":true
}
```

### Use Postman to play with various APIs. Aditionally you can also use curl for various CRUD request in below format.
``` bash
curl -X [GET/POST/PATCH/PUT/DELETE] -d {json_data_to_be_sent} -H 'Content-Type: application/json' http://127.0.0.1:5000/{uri}
```

### To run UnitTest:
$ python unit_test.py
