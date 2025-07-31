from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from src.URLloader import UrlLoader
from src.pipeline import EmbeddingLogic
from src.vectordb_manager import load_or_create_vectorstore

app = FastAPI()

class URLRequest(BaseModel):
    urls: List[str]

class QuestionRequest(BaseModel):
    question: str

@app.post("/embed")
def embed_documents(request: URLRequest):
    try:
        docs = UrlLoader(request.urls)
        # Just store embeddings
        _ = load_or_create_vectorstore(docs)  # It will auto-save
        return {"status": "Embedding and storing successful"}
    except Exception as e:
        print("ERROR in /embed:", e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        # Load only (from previously stored)
        qa_chain = EmbeddingLogic()
        result = qa_chain(request.question)

        return {
            "answer": result['result'],
            "sources": [doc.metadata.get("source", "Unknown") for doc in result['source_documents']]
        }
    except Exception as e:
        print("ERROR in /ask:", e)
        raise HTTPException(status_code=500, detail=str(e))
