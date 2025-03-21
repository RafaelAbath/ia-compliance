# Projeto de Compliance Jurídico com IA

Este projeto tem como objetivo criar um sistema de **Compliance Jurídico** utilizando Inteligência Artificial, integrando técnicas avançadas de IA com a ferramenta **Qdrant** para armazenamento e busca de dados jurídicos. O projeto usa a **OpenAI** para gerar conteúdo jurídico de maneira automatizada e utiliza um banco de dados vetorial para otimizar a pesquisa e o gerenciamento dos documentos.

## Funcionalidades

- **Busca de Jurisprudências**: Permite realizar buscas em um banco de dados de jurisprudências utilizando filtros avançados.
- **Gerenciamento de Documentos**: Armazenamento e recuperação de documentos legais, otimizados com IA.
- **Geração de Peças Jurídicas**: Geração automatizada de peças jurídicas usando modelos de linguagem, com a possibilidade de edição diretamente no editor TinyMCE.
  
## Tecnologias Utilizadas

- **Qdrant**: Banco de dados vetorial para armazenamento e recuperação eficiente de dados.
- **OpenAI**: Utilizado para a geração de texto jurídico e automação de tarefas de compliance.
- **Docker**: Containerização para facilitar o desenvolvimento e a implantação do projeto.
- **Python**: Linguagem de programação principal para o backend.
- **Flask**: Framework para a criação de APIs.
- **TinyMCE**: Editor WYSIWYG para visualização e edição de documentos gerados.

## Como Executar o Projeto com Docker

### Pré-requisitos

Certifique-se de que você tenha as seguintes ferramentas instaladas:

- **Docker**: Para executar o projeto em containers.
- **Docker Compose**: Para facilitar a orquestração dos containers.
- **Git**: Para versionamento de código.

### Passos para Instalar e Rodar com Docker

1. Clone este repositório:
   ```bash
   git clone git@github.com:RafaelAbath/ia-compliance.git
   cd ia-compliance

- **Instruções para utilizar sempre com Docker**, reforçando que o Docker é a forma recomendada para executar o projeto.
- **Dicas para garantir que Docker seja usado consistentemente**, como sempre utilizar `docker-compose` para iniciar o projeto, evitando instalação manual de dependências no ambiente local.
