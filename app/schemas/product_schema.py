
from typing import List
from pydantic import BaseModel, field_validator

# Schema for creating a new product
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    # validate the stock and price should be greater than 0

    @field_validator("stock")
    def validate_stock(cls, v):
        if v <= 0:
            raise ValueError("Stock should be greater than 0")
        return v
    
    @field_validator("price")
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError("Price should be greater than 0")
        return v
    

# Schema for returning product details in API responses
class ProductResponse(ProductCreate):
    id: int  # Include product ID in response

    model_config = {"populate_by_name": True}  # Enable ORM mode for Pydantic
