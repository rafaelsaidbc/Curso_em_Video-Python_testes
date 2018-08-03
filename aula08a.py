import random
inicio = int(input('Digite o primeiro numero da sequencia do sorteio: '))
fim = int(input('Digite o ultimo numero da sequencia do sorteio: '))
num = random.randint(inicio, fim)
sorteados = int(input('Quantos sorteios serão realizados? '))
sort = 0
while sorteados > sort:
    print('O numero sorteado foi {}, parabéns!'.format(num))
    num = random.randint(inicio, fim)
    sorteados -= 1

print('Parabéns a todos os sorteados!')
