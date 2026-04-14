#Inventory System API

#Project Description

This is a simple Inventory Management System built using Flask.
It allows users to:

- Add products using a barcode
- View all products
- View a single product
- Update product details
- Delete products

The system also includes a **CLI (Command Line Interface)** to interact with the API.


#Technologies Used

-Python 3
-Flask
-Requests
-Pytest (for testing)


#Project Structure

inventory_system/
│
├── app.py             
├── cli.py              
├── requirements.txt
├── README.md
└── .gitignore

#Installation & Setup

#1. Clone the repository

git clone https://github.com/PriscillahKamau30/inventory_system.git
cd inventory_system

#2. Create virtual environment

python -m venv venv
source venv/Scripts/activate   # Windows

#3. Install dependencies

pip install -r requirements.txt


#Running the Application

#Start Flask server

python app.py

Server runs on:

http://127.0.0.1:5555


#API Endpoints (Tested with Postman)

#Add Product

POST /inventory

Body:

json
{
  "code": "3017620422003"
}

Response:

- 201 Created
- 400 Bad Request

#Get All Products

GET /inventory

#Get One Product

GET /inventory/<code>


#Update Product

PATCH /inventory/<code>

Body:

json
{
  "name": "Updated Product Name"
}


#Delete Product

DELETE /inventory/<code>

#Postman Testing

All endpoints were tested using Postman:

- POST → 201 Created
- GET → 200 OK
- PATCH → 200 OK
- DELETE → 200 OK
- Error handling → 400 / 404

#CLI Usage

# Add product

python cli.py add 3017620422003

#View all products

python cli.py view

#Get one product

python cli.py get 3017620422003


#Update product

python cli.py update 3017620422003 "New Name"

#Delete product

python cli.py delete 3017620422003


##Notes/Challenges

- External API sometimes returns:

  - 403 Forbidden
  - 429 Too Many Requests
- This was handled by checking response status before parsing JSON
- Data is stored in memory (resets when server restarts)

#Author

Priscillah Kamau
