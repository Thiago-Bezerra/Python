from unicodedata import decimal

aluno = input('Nome do aluno: ')
nota1 = float(input('digite a primeira nota: '))

while nota1 > 10 or nota1 < 0:
    nota1 = float(input('digite a primeira nota: '))

nota2 = float(input('digite a segunda nota: '))
while nota2 > 10 or nota2 < 0:
    nota2 = float(input('digite a segunda nota: '))

media_nota = (nota1 + nota2)/2

print(f'A media do(a) {aluno} é {media_nota}.')
