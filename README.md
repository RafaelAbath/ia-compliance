Compliance Jurídico com OpenAI
Este projeto utiliza OpenAI, Qdrant, e Docker para criar um sistema de compliance jurídico inteligente, permitindo que usuários realizem perguntas jurídicas e obtenham respostas geradas por IA, otimizadas por um mecanismo de busca avançada. O sistema é baseado em FastAPI e utiliza o modelo GPT-3.5 da OpenAI, com integração de Qdrant para armazenamento e recuperação de dados.

Funcionalidades
Consultas Jurídicas: Permite que usuários realizem perguntas jurídicas e obtenham respostas geradas pela IA, com base no modelo GPT-3.5 da OpenAI.

Armazenamento e Recuperação: Utiliza Qdrant para armazenamento de dados e otimização das consultas com recuperação de informações relevantes.

Interface Simples: A API foi construída com FastAPI para proporcionar uma integração rápida e eficiente.

Tecnologias Usadas
OpenAI GPT-3.5: Geração de respostas jurídicas inteligentes.

Qdrant: Banco de dados vetorial utilizado para otimizar a recuperação de dados.

Docker: Contêinerização do projeto para facilitar o ambiente de desenvolvimento e deployment.

FastAPI: Framework para a criação da API.

Python 3.10: Linguagem de programação utilizada no backend.

dotenv: Para carregamento de variáveis de ambiente, como a chave da API da OpenAI.

Uvicorn: Servidor ASGI para executar o FastAPI.

Como Rodar o Projeto
Requisitos
Docker: Necessário para rodar o container de Qdrant e o servidor FastAPI.

Docker Compose: Para orquestrar os containers.

Python 3.10: Para rodar o ambiente de desenvolvimento da aplicação.

Passos para Execução
Clone o repositório:

bash
git clone <URL_DO_REPOSITÓRIO>
cd <diretório_do_repositório>
Criar o arquivo .env: Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

env
OPENAI_API_KEY=sk-<sua_chave_da_openai>
ORGANIZATION=org-<sua_organização_openai>
QDRANT_HOST=localhost
QDRANT_PORT=6333

Build os containers Docker: Com o Docker e Docker Compose instalados, execute o seguinte comando para construir as imagens e rodar os containers:
bash
docker-compose up --build
Isso irá subir dois containers:

Qdrant: Banco de dados vetorial para armazenamento de dados.
App: O servidor FastAPI que executa a API e o cliente OpenAI.
Acesse a API: Após os containers estarem rodando, você pode acessar a API em http://localhost:8000. A documentação da API estará disponível em http://localhost:8000/docs.

Dependências
Este projeto utiliza as seguintes dependências:

qdrant-client
numpy
scikit-learn
torch
transformers
sentence-transformers
fastapi
uvicorn
langchain
langchain-community
langchain-openai
openai
tiktoken
ctransformers
llama-cpp-python
python-dotenv

Você pode instalar as dependências manualmente com:
bash
pip install -r requirements.txt
