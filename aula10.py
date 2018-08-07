n1 = float(input('Qual primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('A média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa')
else:
    print('Média ruim')
