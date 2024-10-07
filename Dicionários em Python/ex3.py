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

def obter_idade(nome):
    if nome in pessoas_idades:
        return f"{nome} tem {pessoas_idades[nome]} anos."
    else:
        return "Nome não encontrado no dicionário."

print(obter_idade("Alice"))
print(obter_idade("Carlos"))
