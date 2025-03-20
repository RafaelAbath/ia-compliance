#!/bin/bash

# Pergunta a mensagem do commit
read -p "Digite a mensagem do commit: " mensagem

# Executa os comandos
git add .
git commit -m "$mensagem"
git push
echo " Commit realizado com sucesso!"