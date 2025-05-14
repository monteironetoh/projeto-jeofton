from combate import criar_jogador, batalha, imprimir_lento

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
