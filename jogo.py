if escolha == "1":
        dano = random.randint(jogador["ataque"] - 5, jogador["ataque"] + 5)
        inimigo["vida"] -= dano
        imprimir_lento(f"Você atacou {inimigo['nome']} e causou {dano} de dano!")
    elif escolha == "2" and jogador["cura"] > 0:
        cura = random.randint(10, 30)
        jogador["vida"] += cura
        jogador["cura"] -= 1
        imprimir_lento(f"Você se curou em {cura} pontos de vida! ({jogador['cura']} curas restantes)")
    else:
        imprimir_lento("Ação inválida ou sem curas restantes.")

def turno_inimigo(jogador, inimigo):
    if inimigo["vida"] <= 0:
        return
    print(f"\nTurno de {inimigo['nome']}!")
    dano = random.randint(inimigo["ataque"] - 3, inimigo["ataque"] + 3)
    jogador["vida"] -= dano
    imprimir_lento(f"{inimigo['nome']} atacou você e causou {dano} de dano!")

def batalha(jogador):
    inimigo = criar_inimigo()
    imprimir_lento(f"\nUm {inimigo['nome']} apareceu com {inimigo['vida']} de vida!")

    while jogador["vida"] > 0 and inimigo["vida"] > 0:
        print(f"\n🧙 {jogador['nome']}: {jogador['vida']} HP")
        print(f"👹 {inimigo['nome']}: {inimigo['vida']} HP")
        turno_jogador(jogador, inimigo)
        turno_inimigo(jogador, inimigo)

    if jogador["vida"] > 0:
        imprimir_lento(f"\nVocê derrotou o {inimigo['nome']}! Parabéns!")
        return True
    else:
        imprimir_lento("\nVocê foi derrotado... Game Over.")
        return False

def jogar():
    print("======================================")
    print("        RPG DE TEXTO - ARENA")
    print("======================================")
    jogador = criar_jogador()

    vitorias = 0
    while jogador["vida"] > 0:
        venceu = batalha(jogador)
        if venceu:
            vitorias += 1
            imprimir_lento(f"Vitórias: {vitorias}")
            continuar = input("\nDeseja continuar lutando? (s/n): ")
            if continuar.lower() != 's':
                break
        else:
            break

    imprimir_lento(f"\nFim do jogo. Você venceu {vitorias} batalha(s).")

if __name__ == "__main__":
    jogar()



