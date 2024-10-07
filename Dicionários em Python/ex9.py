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

def pessoa_mais_nova():
    if pessoas_idades:
        nome_mais_novo = min(pessoas_idades, key=pessoas_idades.get)
        idade_mais_nova = pessoas_idades[nome_mais_novo]
        return f"A pessoa mais nova é {nome_mais_novo} com {idade_mais_nova} anos."
    else:
        return "O dicionário está vazio."

print(pessoa_mais_nova())
