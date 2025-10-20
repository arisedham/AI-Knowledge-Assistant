# app/backend/api_upload.py
import os
import tempfile
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from app.backend.rag_pipeline import process_document, answer_question

router = APIRouter()

# store vectors persistently in this folder
FAISS_DIR = "faiss_store"
os.makedirs(FAISS_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Accepts a document, saves it temporarily, processes into FAISS vector store."""
    try:
        # save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        # process document (chunk + embed + store in FAISS)
        process_document(tmp_path, FAISS_DIR)
        os.remove(tmp_path)

        return {"status": "success", "message": f"File '{file.filename}' ingested."}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@router.post("/query")
async def query(question: str = Form(...)):
    """Accepts a question and returns the model's answer."""
    try:
        answer = answer_question(question, FAISS_DIR)
        return {"question": question, "answer": answer}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
