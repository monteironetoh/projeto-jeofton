import random
import time

# Função para imprimir texto lentamente
def imprimir_lento(texto):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(0.04) # Ajuste este valor para mudar a velocidade da impressão
    print() # Adiciona uma nova linha no final

# Função para criar o personagem do jogador
def criar_jogador():
    nome = input("Digite o nome do seu herói: ")
    jogador = {
        "nome": nome,
        "vida_maxima": 100,
        "vida": 100,
        "ataque": 15,  # Ataque base do jogador
        "cura": 3      # Número inicial de poções de cura
    }
    imprimir_lento(f"Bem-vindo(a), {jogador['nome']}! Sua jornada na arena começa agora.")
    return jogador

# Função para criar um inimigo
def criar_inimigo():
    tipos_inimigos = [
        {"nome": "Goblin Sorrateiro", "vida": 40, "ataque": 8},
        {"nome": "Orc Bruto", "vida": 60, "ataque": 12},
        {"nome": "Esqueleto Guerreiro", "vida": 50, "ataque": 10},
        {"nome": "Lobo das Sombras", "vida": 45, "ataque": 11}
    ]
    # Escolhe um inimigo aleatoriamente da lista
    inimigo_escolhido = random.choice(tipos_inimigos)
    # Retorna uma cópia do dicionário do inimigo para não alterar a lista original
    return dict(inimigo_escolhido)

# Função para o turno do jogador
def turno_jogador(jogador, inimigo):
    print("\n--------------------------------------")
    print("Seu turno:")
    print("1. Atacar")
    print(f"2. Curar ({jogador['cura']} restantes)")
    print("--------------------------------------")
    escolha = input("Escolha sua ação (1 ou 2): ")

    if escolha == "1":
        # Dano do jogador varia um pouco
        dano_base = jogador["ataque"]
        dano = random.randint(max(1, dano_base - 5), dano_base + 5) # Garante que o dano seja pelo menos 1
        inimigo["vida"] -= dano
        imprimir_lento(f"Você atacou {inimigo['nome']} e causou {dano} de dano!")
    elif escolha == "2":
        if jogador["cura"] > 0:
            # Quantidade de cura
            cura = random.randint(20, 30)
            jogador["vida"] += cura
            # Garante que a vida não ultrapasse a vida máxima
            if jogador["vida"] > jogador["vida_maxima"]:
                jogador["vida"] = jogador["vida_maxima"]
            jogador["cura"] -= 1
            imprimir_lento(f"Você usou uma poção e se curou em {cura} pontos de vida!")
            imprimir_lento(f"Você tem {jogador['cura']} poções de cura restantes.")
        else:
            imprimir_lento("Você não tem mais poções de cura!")
            imprimir_lento("Você perdeu a chance de agir neste turno.") # Penalidade por tentar curar sem poção
    else:
        imprimir_lento("Ação inválida. Você perdeu o turno.")

# Função para o turno do inimigo
def turno_inimigo(jogador, inimigo):
    if inimigo["vida"] <= 0:
        return # Inimigo já foi derrotado

    imprimir_lento(f"\nTurno de {inimigo['nome']}!")
    # Dano do inimigo também varia
    dano_base_inimigo = inimigo["ataque"]
    dano = random.randint(max(1, dano_base_inimigo - 3), dano_base_inimigo + 3) # Garante dano mínimo de 1
    jogador["vida"] -= dano
    imprimir_lento(f"{inimigo['nome']} atacou você e causou {dano} de dano!")

# Função principal da batalha
def batalha(jogador):
    inimigo = criar_inimigo()
    imprimir_lento(f"\n🔥 Um {inimigo['nome']} selvagem apareceu com {inimigo['vida']} HP e {inimigo['ataque']} de ATK! 🔥")

    while jogador["vida"] > 0 and inimigo["vida"] > 0:
        print("\n======================================")
        print(f"🧙 {jogador['nome']}: {jogador['vida']}/{jogador['vida_maxima']} HP | Poções: {jogador['cura']}")
        print(f"👹 {inimigo['nome']}: {max(0, inimigo['vida'])} HP") # Garante que a vida do inimigo não seja exibida como negativa
        print("======================================")
        
        turno_jogador(jogador, inimigo)

        if inimigo["vida"] <= 0:
            break # Sai do loop se o inimigo for derrotado

        turno_inimigo(jogador, inimigo)

    if jogador["vida"] > 0:
        imprimir_lento(f"\n🎉 Você derrotou o {inimigo['nome']}! Parabéns! 🎉")
        # Poderia adicionar recompensas aqui (ouro, experiência, etc.)
        jogador["vida"] = jogador["vida_maxima"] # Recupera a vida para a próxima batalha (opcional)
        imprimir_lento("Sua vida foi restaurada para a próxima batalha!")
        return True
    else:
        imprimir_lento(f"\n☠️ Você foi derrotado pelo {inimigo['nome']}... Game Over. ☠️")
        return False

# Função principal do jogo
def jogar():
    print("======================================")
    print("      ⚔️  RPG DE TEXTO - ARENA ⚔️")
    print("======================================")
    jogador = criar_jogador()

    vitorias = 0
    while jogador["vida"] > 0:
        if vitorias > 0: # Pergunta se quer continuar apenas após a primeira vitória
            continuar = input(f"\nVocê tem {vitorias} vitória(s). Deseja continuar lutando? (s/n): ").lower()
            if continuar != 's':
                imprimir_lento("Você decidiu descansar. Até a próxima, guerreiro!")
                break
        
        venceu_batalha = batalha(jogador)
        
        if venceu_batalha:
            vitorias += 1
        else:
            # Se perdeu, o loop de `while jogador["vida"] > 0` vai terminar naturalmente
            break 
            
    imprimir_lento(f"\nFim do jogo. Você conquistou {vitorias} vitória(s). Obrigado por jogar!")

# Executa o jogo
if __name__ == "__main__":
    jogar()
