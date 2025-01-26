from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.product_model import Product
from app.models.order_model import Order
from app.schemas.order_schema import OrderCreate

def create_order(db: Session, order_data: OrderCreate):
    """
    Create a new order with stock validation.

    - Checks if products exist.
    - Validates stock availability.
    - Deducts stock only after successful order creation.
    - Returns 404 if a product does not exist.
    - Returns 400 if stock is insufficient.
    """

    total_price = 0
    product_list = []

    # Validate stock and calculate total price
    for item in order_data.products:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        if not product:
            raise HTTPException(status_code=404, detail=f"Product with ID {item.product_id} not found.")

        if product.stock < item.quantity:
            raise HTTPException(status_code=400, detail=f"Insufficient stock for product {product.name}.")

        total_price += product.price * item.quantity
        product_list.append({"product_id": product.id, "quantity": item.quantity, "price": product.price, "name": product.name, "description": product.description})

    # Create the order
    new_order = Order(products=product_list, total_price=total_price, status="pending")
    db.add(new_order)

    # Deduct stock after order creation
    for item in order_data.products:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        product.stock -= item.quantity

    db.commit()
    db.refresh(new_order)

    return new_order
