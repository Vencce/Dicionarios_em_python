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

def pessoa_mais_velha():
    if pessoas_idades:
        nome_mais_velho = max(pessoas_idades, key=pessoas_idades.get)
        idade_mais_velha = pessoas_idades[nome_mais_velho]
        return f"A pessoa mais velha é {nome_mais_velho} com {idade_mais_velha} anos."
    else:
        return "O dicionário está vazio."

print(pessoa_mais_velha())
