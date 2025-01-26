import pytest

# Test for Home endpoint
def test_home(client):
    """Test the home endpoint to verify the welcome message."""
    response = client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Welcome to the eCommerce API"
    assert "version" in data
    assert data["version"] == "1.0"
    assert "documentation" in data
    assert data["documentation"] == "/docs"

# Test for Health check endpoint
def test_health_check(client):
    """Test the health check endpoint to verify API status."""
    response = client.get("/health")
    
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"
    assert "message" in data
    assert data["message"] == "API is running"
