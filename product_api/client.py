import requests
import json

API_URL = "http://127.0.0.1:8000/api/products/"

# Function to add a new product
def add_product(name, description, price):
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(API_URL + "create/", json=payload)
    if response.status_code == 201:
        print("Product created successfully!")
    else:
        print("Failed to create product:", response.text)

# Function to get all products
def get_products():
    response = requests.get(API_URL)
    if response.status_code == 200:
        products = response.json()
        print("Product List:")
        for product in products:
            print(f"Name: {product['name']}, Description: {product['description']}, Price: {product['price']}")
    else:
        print("Failed to retrieve products:", response.text)

# Example interaction
if __name__ == '__main__':
    # Add some products
    add_product("Product1", "Description for product 1", 10.5)
    add_product("Product2", "Description for product 2", 15.75)

    # Get and print all products
    get_products()
