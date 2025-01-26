from pydantic import BaseModel, field_validator
from typing import List

# Schema for individual order items (product ID and quantity)
class OrderItem(BaseModel):
    product_id: int
    quantity: int

    @field_validator("quantity")
    def validate_quantity(cls, v):
        if v <= 0:
            raise ValueError("Quantity should be greater than 0")
        return v

# Schema for creating a new order
class OrderCreate(BaseModel):
    products: List[OrderItem]
        

# Schema for returning order details in API responses
class OrderResponse(BaseModel):
    id: int
    total_price: float
    status: str 
    products: List[dict]
    model_config = {"populate_by_name": True}
