from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

def answer_question(pergunta: str):
    print(f"Pergunta recebida: {pergunta}")  # Log da pergunta recebida
    
    # Obtendo as variáveis de ambiente
    qdrant_url = os.getenv("QDRANT_HOST", "localhost")  # Defina o valor padrão para 'localhost' se não houver variável
    qdrant_port = os.getenv("QDRANT_PORT", "6333")  # Defina o valor padrão para '6333' se não houver variável
    
    # Garantir que o valor de 'port' seja inteiro
    qdrant_port = int(qdrant_port)
    
    # Configuração dos embeddings com a chave da OpenAI
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    # Construir a URL completa do Qdrant
    qdrant_full_url = f"{qdrant_url}:{qdrant_port}"
    
    # Correção: Usar 'from_documents' para inicializar o Qdrant corretamente
    client = Qdrant.from_documents(
        embedding_function=embeddings,
        collection_name="compliance_docs",  # Nome da coleção no Qdrant
        url=qdrant_full_url  # Passar a URL do Qdrant
    )

    # Cria o retriever para buscar documentos relacionados
    retriever = client.as_retriever()

    # Recupera os documentos relevantes para a pergunta
    docs = retriever.get_relevant_documents(pergunta)
    print(f"Documentos recuperados: {len(docs)}")  # Log dos documentos recuperados

    # Configuração do modelo de chat da OpenAI para responder
    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))

    # Cria a cadeia RAG (Retrieval-Augmented Generation)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # Tipo de cadeia utilizada (stuff)
        retriever=retriever  # O retriever que busca os documentos
    )

    # Faz a pergunta e obtém a resposta
    resultado = qa_chain.run(pergunta)
    print(f"Resposta gerada: {resultado}")  # Log da resposta gerada

    return resultado
