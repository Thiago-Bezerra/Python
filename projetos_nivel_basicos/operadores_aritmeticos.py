n1 = int(input('um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
sub = n1 - n2
di = n1 // n2
dr = n1 % n2
p = n1 ** n2
print(f'A soma é {s}, a divisão é {d:.2f}, a subtração é {sub}')
print('A parte inteira é {}, resto da visão é {}'.format(di, dr), end=' ')
print('A multiplicação é ', m, '\n e a potência é ', p)
