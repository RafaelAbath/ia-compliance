def limpar_texto(texto):
    return texto.strip().replace("\n", " ")

# Exemplos de expansão:
def normalizar_texto(texto):
    return limpar_texto(texto).lower()
s