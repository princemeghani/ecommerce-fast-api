from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.product_service import get_products, create_product
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.core.database import get_db

router = APIRouter()

# Endpoint to fetch all products
@router.get("/products", response_model=list[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    return get_products(db)

# Endpoint to add a new product
@router.post("/products", response_model=ProductResponse, status_code=201)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)
