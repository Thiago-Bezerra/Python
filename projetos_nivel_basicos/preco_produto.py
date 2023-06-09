preco_produto = float(input('Digite o preço original do produto: R$ '))
desconto = 0.05
desconto_produto = preco_produto * desconto
novo_preco = preco_produto - desconto_produto

print(f'O preço com o desconto de 5% fica por R$ {novo_preco:.2f}')
