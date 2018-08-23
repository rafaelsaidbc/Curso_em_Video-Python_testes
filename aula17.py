num = [1, 2, 3, 4]
print('num = ', num)
print('print(num) = ', num)
num[2] = 10
print('num[2] = 10 = ', num)
num.append(5)
print('num.append(5) = ', num)
num.sort(reverse=True)
print('num.sort(reverse=True) = ', num)
print('print(len(num)) = ', len(num))
num.insert(2, 0)
print('num.insert(2, 0) = ', num)
num.pop()
print('num.pop() = ', num)
num.pop(2)
print('num.pop(2) = ', num)
num.insert(2, 2)
print('num.insert(2, 2) = ', num)
num.remove(2)
print('num.remove(2) = ', num)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for indice, valor in enumerate(valores):
    print(f'Na posição {indice}, tem o valor {valor}...')
print('Cabô!')
lista_criada = []
for contador in range(0, 5):
    lista_criada.append(int(input('Insira um valor na lista: ')))
print('print(lista_criada) = ', lista_criada)
a = [1, 2, 3, 4]
b = a[:]
print('b = a[:] - cria uma cópia da lista a', b)
