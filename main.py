from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.rag_pipeline import answer_question
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="Compliance Jurídico RAG API")

import os
print(os.getenv("OPENAI_API_KEY"))


# Definir o modelo Pydantic para receber a pergunta no corpo da requisição
class PerguntaModel(BaseModel):
    pergunta: str

@app.get("/")
def root():
    return {"message": "API de Compliance Jurídico com RAG"}


@app.post("/perguntar/")
def perguntar(pergunta: PerguntaModel):
    try:
        print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")
        resposta = answer_question(pergunta.pergunta)
        return {
            "pergunta": pergunta.pergunta,
            "resposta": resposta
        }
    
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

