variavel = 1  # define uma variavel qualquer que recebe o valor 1
while variavel < 10:  # enquanto o valor da variável for menor que 10
    print(variavel)  # executa o comando print(variavel)
    variavel += 1  # incrementa a variavel em +1
print('Cabô!')  # imprime Cabô para mostrar o fim da execução do script

print('=' * 20)
print('Mais um exemplo')
numero = 1
while numero != 0:
    numero = int(input('Digite um valor ou [0] para encerrar: '))
    print('Você digitou o número [{}]!'.format(numero))
print('Cabôôô.')

print('=' * 20)
print('Mais um exemplo legal')
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um número: '))
    print('Você digitou o número: {}'.format(n))
    resposta = str(input('Quer continuar? [S/N]').upper())
print('Você encerrou o programa.')

print('=' * 20)
print('Mais um exemplo')
x = 1
pares = 0
impares = 0
while x != 0:
    x = int(input('Digite um valor ou [0] para encerrar: '))
    if x != 0:
        if x % 2 == 0:
            pares += 1
        else:
            impares += 1
print('Você digitou {} pares e {} ímpares!'.format(pares, impares))
