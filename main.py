from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()  # Carregar as variáveis do .env

# Inicializando o cliente OpenAI com a chave da API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), onizatirgaon=os.getenv("ORGANIZATION"))


# Inicializando o FastAPI
app = FastAPI(title="Compliance Jurídico com OpenAI")



# Modelo Pydantic para receber a pergunta
class PerguntaModel(BaseModel):
    pergunta: str

@app.get("/")
def root():
    return {"message": "API de Compliance Jurídico com OpenAI"}

@app.post("/pergunta/")
def perguntar_openai(pergunta: PerguntaModel):
    try:
        # Fazendo uma chamada para o modelo GPT-3.5 da OpenAI para gerar uma resposta
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Usando o modelo GPT-3.5 Turbo
            messages=[
                {"role": "system", "content": "Você é um assistente jurídico."},
                {"role": "user", "content": pergunta.pergunta}
            ]
        )

        resposta = response.choices[0].message.content.strip()

        return {
            "resposta": resposta
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/perguntar/")  # A rota original que faz o processamento com RAG
def perguntar(pergunta: PerguntaModel):
    try:
        resposta = answer_question(pergunta.pergunta)
        return {
            "pergunta": pergunta.pergunta,
            "resposta": resposta
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
