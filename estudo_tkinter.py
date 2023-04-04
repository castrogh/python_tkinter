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

    lbl_cotacoes["text"] = texto #ao utlizar o ["text"], estou modificando o parâmetro text da variavel lbl_cotacoes para o conteúdo da variável texto


janela = Tk()

janela.title("Cotações - US$, EUR e BTC")

lbl_clique_btn = Label(janela, text="Clique no botão abaixo para ver as cotações")
lbl_clique_btn.grid(column=0, row=0)

btn_cotacao = Button(janela, text="Clique Aqui!", command = pegar_cotacoes) #ao passar a função pegar_cotacoes, como um parâmetro, sem os (), estou informando que ela só deve ser executada quando o botão for clicado, caso fosse passada com os (), a função seria executada automaticamente
btn_cotacao.grid(column=0, row=1)

lbl_cotacoes = Label(janela, text="As cotações serão mostradas aqui")
lbl_cotacoes.grid(column=0, row=2)


janela.mainloop()