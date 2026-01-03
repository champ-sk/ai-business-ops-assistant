from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(
    title="AI Business Operations Assistant",
    version="0.1.0"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "AI Business Ops Assistant running"}
