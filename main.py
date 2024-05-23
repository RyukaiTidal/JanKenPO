from classes import *

print("PEDRA PAPEL E TESOURA!")

jogo = Jogo()
print("Bem vindo a jogo da velha!")

while True:
    escolha = input("Escolha entre Pedra, Papel, e Tesoura!\n-")
    if escolha in "Pedra" or escolha == "pedra":
        jogo.player = "Pedra"
        break
    if escolha in "papel" or escolha == "Papel":
        jogo.player = "Papel"
        break
    if escolha == "tesoura" or escolha == "Tesoura":
        jogo.player = "Tesoura"
        break

jogo.decisaoJogo()
resultado = jogo.resultadoJogo()

print(resultado)