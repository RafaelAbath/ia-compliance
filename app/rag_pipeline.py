import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def answer_question(pergunta: str):
    qdrant_url = os.getenv("QDRANT_HOST", "localhost")
    qdrant_port = os.getenv("QDRANT_PORT", "6333")

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

    # Conectando ao Qdrant com a collection "compliance_docs"
    qdrant = Qdrant(
        embedding_function=embeddings,
        url=f"http://{qdrant_url}:{qdrant_port}",
        collection_name="compliance_docs"
    )

    # Cria o retriever para buscar documentos relacionados
    retriever = qdrant.as_retriever()

    # Instancia o modelo de chat
    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))

    # Cria a cadeia RAG (Retrieval-Augmented Generation)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )

    # Faz a pergunta e obtém a resposta
    resultado = qa_chain.run(pergunta)

    return resultado
