from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
import os

def carregar_documento(caminho_arquivo):
    loader = TextLoader(caminho_arquivo, encoding='utf-8')
    documentos = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs_divididos = splitter.split_documents(documentos)

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

    qdrant_url = os.getenv("QDRANT_HOST", "localhost")
    qdrant_port = os.getenv("QDRANT_PORT", "6333")

    qdrant = Qdrant.from_documents(
        docs_divididos,
        embeddings,
        url=f"http://{qdrant_url}:{qdrant_port}",
        collection_name="compliance_docs"
    )

    print(f"Ingestão de {len(docs_divididos)} documentos concluída!")

if __name__ == "__main__":
    caminho = "data/compliance/seu_documento.txt"
    carregar_documento(caminho)
