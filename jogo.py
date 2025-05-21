import random
import time

def imprimir_lento(texto, delay=0.02):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()

def criar_jogador():
    nome = input("Digite o nome do seu herói: ")
    return {"nome": nome, "vida": 100, "ataque": 15, "cura": 3}

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
