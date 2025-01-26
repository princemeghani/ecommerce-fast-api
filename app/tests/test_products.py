import pytest
from app.models.product_model import Product
from fastapi import HTTPException

# Test Fixture to create a product
@pytest.fixture
def create_test_product(db):
    """Create and return a test product."""
    product = Product(name="Test Product", description="A test product", price=10.0, stock=5)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Test for adding a new product
def test_add_product(client, db):
    """Test adding a new product successfully."""
    response = client.post("/products", json={
        "name": "Laptop",
        "description": "A high-performance laptop",
        "price": 1200.00,
        "stock": 10
    })
    
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["price"] == 1200.00
    assert data["stock"] == 10

# Test for missing required fields (e.g., 'name' is required)
def test_add_product_missing_name(client, db):
    """Test adding a product with missing name."""
    response = client.post("/products", json={
        "description": "A product with no name",
        "price": 1500.00,
        "stock": 5
    })
    
    assert response.status_code == 422  # Unprocessable Entity for missing required fields
    assert "name" in response.json()["detail"][0]["loc"]

# Test for invalid price (e.g., negative price)
def test_add_product_invalid_price(client, db):
    """Test adding a product with an invalid (negative) price."""
    response = client.post("/products", json={
        "name": "Invalid Price Product",
        "description": "Product with a negative price",
        "price": -100.00,  # Invalid price
        "stock": 5
    })
    
    assert response.status_code == 422  # Unprocessable Entity for invalid data
    assert "price" in response.json()["detail"][0]["loc"]

# Test for invalid stock (e.g., negative stock)
def test_add_product_invalid_stock(client, db):
    """Test adding a product with invalid (negative) stock."""
    response = client.post("/products", json={
        "name": "Invalid Stock Product",
        "description": "Product with a negative stock",
        "price": 100.00,
        "stock": -5  # Invalid stock
    })
    
    assert response.status_code == 422  # Unprocessable Entity for invalid data
    assert "stock" in response.json()["detail"][0]["loc"]

# Test for getting all products (valid response)
def test_get_all_products(client, db, create_test_product):
    """Test retrieving all products."""
    response = client.get("/products")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test for getting a product by ID that doesn't exist (404)
def test_get_product_not_found(client, db):
    """Test retrieving a product by an ID that doesn't exist."""
    response = client.get("/products/9999")  # Assuming 9999 does not exist
    
    assert response.status_code == 404  # Not Found

