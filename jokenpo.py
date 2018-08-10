import random

jogador = int(input('Escolha sua jogada:\n[0] Tesoura\n[1] Papel\n[2] Pedra\n'))
computador = random.randint(0, 2)
tesoura = 0
papel = 1
pedra = 2
if jogador == tesoura:
    if computador == tesoura:
        print('Ambos escolheram tesoura, deu empate.')
    elif computador == papel:
        print('Você escolheu tesoura e o computador papel, você venceu.')
    elif computador == pedra:
        print('Você escolheu tesoura e o computador pedra, você perdeu')
elif jogador == papel:
    if computador == tesoura:
        print('Você escolheu papel e o computador tesoura, você perdeu.')
    elif computador == papel:
        print('Ambos escolheram papel, deu empate.')
    elif computador == pedra:
        print('Você escolheu papel e o computador pedra, você venceu.')
elif jogador == pedra:
    if computador == tesoura:
        print('Você escolheu pedra e o computador tesoura, você venceu.')
    elif computador == papel:
        print('Você escolheu pedra e o computador papel, você perdeu.')
    elif computador == pedra:
        print('Ambos escolheram pedra, deu empate.')
else:
    print('Opção inválida. Jogue novamente.')
