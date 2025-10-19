from fastapi import FastAPI
from app.backend.api_upload import router as upload_router

app = FastAPI(title="AI Knowledge Assistant API")

app.include_router(upload_router, prefix="/api")
