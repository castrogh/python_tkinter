import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    print(texto)

pegar_cotacoes()


janela = Tk()

janela.title("Cotações - US$, EUR e BTC")

txt_cotacao = Label(janela, text="Clique no botão abaixo para ver as cotações")
txt_cotacao.grid(column=0, row=0)

janela.mainloop()