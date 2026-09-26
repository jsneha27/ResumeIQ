from fastapi import FastAPI

from backend.app.api.health import router as health_router
from backend.app.api.resume import router as resume_router


app = FastAPI(
    title="ResumeIQ API",
    description="AI-powered Resume & Job Intelligence Platform",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(resume_router)
