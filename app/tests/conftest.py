import pytest
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base, get_db 
from fastapi.testclient import TestClient
from app.main import app  

# Load environment variables from .env file
load_dotenv()

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    """Create a new test database session"""
    Base.metadata.create_all(bind=engine)  # Create all tables (including products)
    session = TestingSessionLocal()
    try:
        yield session  # Provide the session for testing
    finally:
        session.rollback()  # Rollback any changes made during the test
        session.close()     # Close the session after the test is done
        Base.metadata.drop_all(bind=engine)  # Drop the tables after each test

@pytest.fixture(scope="function")
def client(db):
    """Create a test client with overridden database dependency."""
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
