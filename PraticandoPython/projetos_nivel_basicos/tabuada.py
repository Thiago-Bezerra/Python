numero = int(input('Digite um número inteiro: '))
limite = int(input(f'Qual o limite da tabuada {numero}: '))
cont = 0
while cont < limite + 1:
    tabuada = numero * cont
    print('{1} x {0} = {2}'.format(cont, numero, tabuada))
    cont += 1
print('-------------------------------------------------------------------')
for i in range(0, limite + 1):
    tabuada = numero * i
    print(f'{numero} x {i:2} = {tabuada}')

