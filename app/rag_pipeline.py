from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from qdrant_client import QdrantClient  # <- importante!
import os

def answer_question(pergunta: str):
    print(f"Pergunta recebida: {pergunta}")  # Log da pergunta recebida
    
    # Obtendo as variáveis de ambiente
    qdrant_url = os.getenv("QDRANT_HOST", "localhost")
    qdrant_port = os.getenv("QDRANT_PORT", "6333")
    
    # Garantir que o valor de 'port' seja inteiro
    qdrant_port = int(qdrant_port)
    
    # Configuração dos embeddings com a chave da OpenAI
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    # Cria o cliente de conexão com o Qdrant
    client = QdrantClient(
        url=f"http://{qdrant_url}",
        port=qdrant_port
    )

    vectorstore = Qdrant(
    client=client,
    collection_name="compliance_docs",
    embeddings=embeddings
)


    # Cria o retriever para buscar documentos relacionados
    retriever = vectorstore.as_retriever()


    # Recupera os documentos relevantes para a pergunta
    docs = retriever.get_relevant_documents(pergunta)
    print(f"Documentos recuperados: {len(docs)}")  # Log dos documentos recuperados

    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))

    qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)


    # Faz a pergunta e obtém a resposta
    resultado = qa_chain.run(pergunta)
    print(f"Resposta gerada: {resultado}")

    return resultado
