produtos = ('Arroz', 10.25, 'Feijão', 6.53, 'Macarrão', 7.54, 'Azeite', 15.21,
            'Carne', 32.57)
for produto in produtos:
    if produtos.index(produto) % 2 == 0:
        print(f'{produto:<10}', end='.' * 10)
    if produtos.index(produto) % 2 != 0:
        print(f'{produto:>8}')
