cores = {'limpa': '\033[m',
         'azul': '\033[34',
         'amarelo': '\033[33m',
         'fla': '\033[1;30;41m'}
nome = 'Rafael'
print('Oi {}.'.format(cores['fla'], nome, cores['limpa']))

print('\033[4;30;41mFlamengo\033[m')
print('\033[4;33;44mFlamengo\033[m')
print('\033[1;35;43mFlamengo\033[m')
print('\033[30;42mFlamengo\033[m')
print('\033[mFlamengo\033[m')
print('\033[7;30mFlamengo\033[m')
print('\033[1;30;41mFlamengo\033[m')
