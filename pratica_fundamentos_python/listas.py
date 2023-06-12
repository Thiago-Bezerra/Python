lista = [1, 2, 3, 5]
lista_animal = ['gato', 'leão', 'galo']

print(lista_animal[2])
soma = 0
for i in lista:
    print(i)
    soma += i
print(soma)
print(sum(lista))

print(max(lista_animal))
print(min(lista_animal))

if 'lobo' in lista_animal:
    print('existe')
else:
    print('não existe')
    lista_animal.append('lobo')
    print(lista_animal)


