from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    """Home endpoint with welcome message"""
    return {
        "message": "Welcome to the eCommerce API",
        "version": "1.0",
        "documentation": "/docs"
    }

@router.get("/health")
async def health_check():
    """Health check endpoint to verify API status"""
    return {"status": "healthy", "message": "API is running"}

