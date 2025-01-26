from sqlalchemy import Column, Integer, Float, String, JSON
from app.core.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    products = Column(JSON, nullable=False)  
    total_price = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="pending")  # Possible values: 'pending', 'completed'
