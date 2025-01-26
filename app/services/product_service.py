from sqlalchemy.orm import Session
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate

def get_products(db: Session):
    """Fetch all products from the database."""
    return db.query(Product).all()

def create_product(db: Session, product_data: ProductCreate):
    """Create a new product in the database."""
    new_product = Product(**product_data.model_dump())  
    db.add(new_product) 
    db.commit()  
    db.refresh(new_product)  
    return new_product
