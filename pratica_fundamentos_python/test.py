# def sacar(valor):
#     saldo = 500
#     if saldo >= valor:
#         print("valor sacado!")

#     print("Valor insuficiente...")

# def depositar(valor):
#     saldo = 500
#     if saldo > 0:
#         valor += saldo
#         print(f"O valor da conta è {valor}")

# texto = input("Digite uma frase ou palavra: ")
# VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end=" ") #sep= "-")
# else:
#     print()

# for numero in range(0, 51, 5):
#     print(numero, end=" ")#sep=";")

# nome = "Thiago"

# print(nome.upper())
# print(nome.lower())
# print(nome.title())
# print(nome.ljust(10," "))
# print(nome.center(12,"!"))
# print("-".join(nome))

# nome ="thiago"
# idade = 28
# profissao= "Professor"
# liguagem = "python"

# # metodos de cocatenação 
# # 1 primeiro

# print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, liguagem))
# print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}." .format(nome, idade, profissao, liguagem))
# print(f"""Olá, me chamo {nome}. Eu tenho {idade} anos de idade, 
#       trabalho como {profissao} e estou matriculado no curso de {liguagem}.""")

# test = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
# print(test)

# carros = ("gol")
# print(isinstance(carros, tuple))

# T = int(input())

# for i in range(T):
#   N = int(input())
#   K = int(input())
#   garrafas_cheias = (N//K)+(N%K)
  
#   print(garrafas_cheias)

# print((4000//7)+(4000%7))

class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())

class Bar(Foo):
    def hello(self):
        return super().hello()

bar = Bar()
bar.hello()