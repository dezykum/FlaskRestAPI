# FlaskRestAPI
In this project, I have worked with Flask to create REST API for all CRUD operations for 
Product Management System. I have used SQLAlchemy module for managing the DB.

How to run this project:

1. Download the project, unzip it, go to the folder path in command prompt.

2. first run pip install on the requirements.txt file to install all the requirements.
   pip install -r requirements.txt

3. To run the app with database, run the ProductsRestApi.py file
   python ProductRestApi.py 

5. A server will be opened on port 5000

6. Open Postman and play with various REST API requests. Aditionally you can also use curl for various CRUD request in below format.
    curl -X [GET/POST] -d {json_data_to_be_sent} -H 'Content-Type: application/json' http://127.0.0.1:5000/{uri}

7. For unit testing, run the Unittest.py file
    python Unittest.py 
