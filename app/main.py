from fastapi import FastAPI
from app.core.database import engine, Base
from app.routes import home_routes, product_routes, order_routes

app = FastAPI()

# Create database tables on startup
Base.metadata.create_all(bind=engine)

# Register API routes
app.include_router(home_routes.router)
app.include_router(product_routes.router)
app.include_router(order_routes.router)
