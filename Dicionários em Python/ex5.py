pessoas_idades = {
    "Alice": 25,
    "Bruno": 30,
    "Carla": 22,
    "Daniel": 28,
    "Eduardo": 35,
    "Fernanda": 27,
    "Gabriel": 21,
    "Helena": 24,
    "Isabela": 29,
    "João": 31
}

def remover_pessoa(nome):
    if nome in pessoas_idades:
        del pessoas_idades[nome]
        return f"{nome} foi removido(a) do dicionário."
    else:
        return "Nome não encontrado no dicionário."

print(remover_pessoa("Bruno"))
print(remover_pessoa("Carlos"))
