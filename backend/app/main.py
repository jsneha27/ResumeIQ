from fastapi import FastAPI

app = FastAPI(
    title="ResumeIQ API",
    description="AI-powered Resume & Job Intelligence Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ResumeIQ API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }