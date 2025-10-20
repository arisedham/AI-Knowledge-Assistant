# app/backend/main.py
from fastapi import FastAPI
from app.backend.api_upload import router as upload_router

app = FastAPI(title="AI Knowledge Assistant API")

# include the router defined in api_upload.py
app.include_router(upload_router, prefix="/api", tags=["RAG"])