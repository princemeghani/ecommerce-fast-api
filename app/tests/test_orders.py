import pytest
from app.models.product_model import Product

@pytest.fixture
def create_test_product(db):
    """Create and return a test product."""
    product = Product(name="Test Product", description="A test product", price=10.0, stock=5)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def test_place_order_success(client, db, create_test_product):
    """Test placing an order successfully."""
    product_id = create_test_product.id
    response = client.post("/orders", json={
        "products": [{"product_id": product_id, "quantity": 2}]
    })
    
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "pending"
    assert data["total_price"] == create_test_product.price * 2

def test_place_order_insufficient_stock(client, db, create_test_product):
    """Test placing an order when stock is insufficient."""
    product_id = create_test_product.id
    response = client.post("/orders", json={
        "products": [{"product_id": product_id, "quantity": 100}]  # Exceeds stock
    })
    
    assert response.status_code == 400
    assert response.json()["detail"] == "Insufficient stock for product Test Product."

def test_place_order_missing_product_id(client, db):
    """Test placing an order with a missing product ID."""
    response = client.post("/orders", json={
        "products": [{"quantity": 2}]  # Missing product_id
    })
    
    assert response.status_code == 422  # Unprocessable Entity
    assert "product_id" in response.json()["detail"][0]["loc"]

def test_place_order_invalid_product_id(client, db):
    """Test placing an order with an invalid product ID."""
    product_id = 9999
    response = client.post("/orders", json={
        "products": [{"product_id": product_id, "quantity": 2}]  # Non-existent product
    })
    
    assert response.status_code == 404  # Not Found
    assert response.json()["detail"] == f"Product with ID {product_id} not found."

def test_place_order_missing_quantity(client, db, create_test_product):
    """Test placing an order with a missing quantity."""
    product_id = create_test_product.id
    response = client.post("/orders", json={
        "products": [{"product_id": product_id}]  # Missing quantity
    })
    
    assert response.status_code == 422  # Unprocessable Entity
    assert "quantity" in response.json()["detail"][0]["loc"]

def test_place_order_invalid_quantity(client, db, create_test_product):
    """Test placing an order with an invalid quantity (negative)."""
    product_id = create_test_product.id
    response = client.post("/orders", json={
        "products": [{"product_id": product_id, "quantity": -1}]  # Invalid quantity
    })
    print(response.json()["detail"][0])
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "Value error, Quantity should be greater than 0"


