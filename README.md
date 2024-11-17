# Django E-Commerce Project

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <https://github.com/keith-oruo/API-BBIT-2.2-A-CAT-2.git>
   cd ecommerce
2. pip install django
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver
6. python manage.py createsuperuser

# Product API

This is a simple REST API built with Django and Django REST Framework to manage products.

## Setup and Running the API

1. Install the required dependencies:
    ```bash
    pip install django djangorestframework
    ```

2. Create and apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Run the Django server:
    ```bash
    python manage.py runserver
    ```

4. The API will be running at `http://127.0.0.1:8000/api/`.

## API Endpoints

- **POST /api/products/create/**: Creates a new product.  
  Request body should be a JSON object with `name`, `description`, and `price` fields.
  Example request:
  ```json
  {
    "name": "Product1",
    "description": "A sample product",
    "price": 20.5
  }
