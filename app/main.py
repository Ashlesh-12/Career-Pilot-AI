from fastapi import FastAPI
from app.routers.careers import router as careers_router
from app.routers.jobs import router as jobs_router

app = FastAPI(
    title = "CareerPilot AI",
    description="AI-powered career discovery platform",
    version="1.0.0",
)

app.include_router(
    careers_router,
    prefix="/api/v1",
    tags=["Careers"],
)

app.include_router(
    jobs_router,
    prefix="/api/v1",
    tags=["Jobs"], 
)