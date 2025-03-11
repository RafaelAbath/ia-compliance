from fastapi import FastAPI
from app.rag_pipeline import answer_question
from dotenv import load_dotenv
load_dotenv()
app = FastAPI(title="Compliance Jurídico RAG API")

import os
print(os.getenv("OPENAI_API_KEY"))


@app.get("/")
def root():
    return {"message": "API de Compliance Jurídico com RAG"}

@app.post("/perguntar/")
def perguntar(pergunta: str):
    try:
        resposta = answer_question(pergunta)
        return {
            "pergunta": pergunta,
            "resposta": resposta
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
