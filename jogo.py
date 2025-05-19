def jogar():
    print("======================================")
    print("        RPG DE TEXTO - ARENA")
    print("======================================")
    jogador = criar_jogador()
    if __name__ == "__main__":
        def criar_inimigo():
    inimigos = ["Goblin", "Esqueleto", "Orc", "Slime", "Dragão Bebê"]
    nome = random.choice(inimigos)
    vida = random.randint(30, 80)
    ataque = random.randint(8, 20)
    return {"nome": nome, "vida": vida, "ataque": ataque}

def turno_jogador(jogador, inimigo):
    print("\nSeu turno!")
    print("1 - Atacar")
    print("2 - Curar")
    escolha = input("Escolha sua ação: ")
