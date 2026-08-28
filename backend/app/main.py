from fastapi import FastAPI
from app.api.routes import health


app = FastAPI(
    title="NurseFlow API",
    description="Backend API for NurseFlow.",
    version="0.1.0",
)

app.include_router(
    health.router,
    prefix="/api/v1",
)