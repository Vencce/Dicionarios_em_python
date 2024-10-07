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

def atualizar_idade(nome, nova_idade):
    if nome in pessoas_idades:
        pessoas_idades[nome] = nova_idade
        return f"A idade de {nome} foi atualizada para {nova_idade} anos."
    else:
        return "Nome não encontrado no dicionário."

print(atualizar_idade("Alice", 26))
print(atualizar_idade("Carlos", 40))
