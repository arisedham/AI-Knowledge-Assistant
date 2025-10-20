import os
import tempfile
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.backend.rag_pipeline import process_document, answer_question

router = APIRouter()

# Persistent vector store folder
FAISS_DIR = "faiss_store"
os.makedirs(FAISS_DIR, exist_ok=True)

# --- Pydantic model for /query request ---
class QueryRequest(BaseModel):
    question: str


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Handles file upload and processes it into FAISS embeddings."""
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        # Process the document (chunk + embed + save to FAISS)
        process_document(tmp_path, FAISS_DIR)
        os.remove(tmp_path)

        return {"status": "success", "message": f"File '{file.filename}' ingested."}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@router.post("/query")
async def query(request: QueryRequest):
    """Accepts a question and returns the model's answer."""
    try:
        question = request.question
        answer = answer_question(question, FAISS_DIR)
        return {"question": question, "answer": answer}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
