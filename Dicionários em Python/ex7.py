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

def media_idades():
    total_idades = sum(pessoas_idades.values())
    quantidade = len(pessoas_idades)
    return total_idades / quantidade if quantidade > 0 else 0

print(media_idades())
