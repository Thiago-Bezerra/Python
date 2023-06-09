teste_numero = int(input('Teste de para saber a quantidade d numero primos, digite um número: '))

total_numeros = 0

for numero in range(teste_numero + 1):
    divisores = 0
    for i in range(1, numero + 1):
        resto = numero % i
        if resto == 0:
            divisores += 1
    if divisores == 2:
        print(numero)
        total_numeros += 1
print('tem um total de {} números primos'.format(total_numeros))
