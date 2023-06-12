def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write('\n primeira linha')
    arquivo.close()
