from tkinter import Tk, Label, Button
import requests


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotatacao_dolar = requisicao_dic['USDBRL']['bid']
    cotatacao_euro = requisicao_dic['EURBRL']['bid']
    cotatacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dolar: {cotatacao_dolar}
    Eurp: {cotatacao_euro}
    BTC: {cotatacao_btc}
    '''
    texto_cotacoes["text"] = texto


windows = Tk()
windows.title('Cotacao Atual das Moedas')
texto_orientacao = Label(windows, text='Clique no botao para exibir a cotacao')
texto_orientacao.grid(row=0, column=0, columnspan=4)
botao_inicia = Button( 
    windows, text='exibir cotacao', command=pegar_cotacoes
)
botao_inicia.grid(row=1, column=0, columnspan=2)

texto_cotacoes = Label(windows, text="")
texto_cotacoes.grid(row=2, column=0)


windows.mainloop()