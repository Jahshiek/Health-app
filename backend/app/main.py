from fastapi import FastAPI

from app.api.routes import health, sessions

app = FastAPI(
    title="NurseFlow API",
    description="Backend API for NurseFlow.",
    version="0.1.0",
)

# health routes
app.include_router(health.router, prefix="/api/v1")

# study session routes
app.include_router(sessions.router, prefix="/api/v1")