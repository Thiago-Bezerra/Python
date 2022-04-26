
numero = int(input('Entre com o número: '))
dividores = 0

for i in range(1, numero + 1):
    resto = numero % i
    if resto == 0:
        dividores += 1

print(f'O número {numero} tem {dividores} divisores.')

if dividores == 2:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')
