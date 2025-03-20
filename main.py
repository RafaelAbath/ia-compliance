from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Inicializando o FastAPI
app = FastAPI(title="Compliance Jurídico com OpenAI")

# Carrega a chave da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Modelo Pydantic para receber a pergunta
class PerguntaModel(BaseModel):
    pergunta: str

@app.get("/")
def root():
    return {"message": "API de Compliance Jurídico com OpenAI"}

@app.post("/perguntar-openai/")
def perguntar_openai(pergunta: PerguntaModel):
    try:
        # Fazendo uma chamada para o modelo GPT-3 da OpenAI para gerar uma resposta
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Usando o modelo GPT-3.5 Turbo
            messages=[
                {"role": "system", "content": "Você é um assistente jurídico."},
                {"role": "user", "content": pergunta.pergunta}
            ]
        )
        
        resposta = response['choices'][0]['message']['content'].strip()
        
        return {
            "pergunta": pergunta.pergunta,
            "resposta": resposta
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/perguntar/")  # A rota original que faz o processamento com RAG
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
