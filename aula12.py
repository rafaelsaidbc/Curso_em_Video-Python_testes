nome = str(input('Qual o seu nome? '))
if nome == 'Rafael':
    print('Bonito nome')
elif nome == 'João' or nome == 'Maria':
    print('Seu nome é comum no Brasil.')
else:
    print('Seu nome e legal.')
print('Tenha um bom dia, {}!'.format('\033[1;30;41m' + nome + '\033[m'))
