conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
conjunto_intersecao = conjunto.intersection(conjunto2)
print(conjunto_intersecao)
conjunto_diferenca = conjunto.difference(conjunto2)
print(conjunto_diferenca)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(conjunto_diferenca2)
conjunto_diferenca_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_diferenca_simetrica)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_b.issubset(conjunto_a)
print(conjunto_subset)

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'leão']
print(lista)
conjunto_animal = set(lista)
print(conjunto_animal)
