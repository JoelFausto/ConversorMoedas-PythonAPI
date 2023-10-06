# Importando as bibliotecas
from tkinter import *
import requests
import json
from PIL import Image, ImageTk

class ConversorMoedas:

    def __init__(self, root=None):
        
        imagem_pil = Image.open("image.png")
        largura, altura = 200, 200
        imagem_pil = imagem_pil.resize((largura, altura), Image.ANTIALIAS)
        self.imagem = ImageTk.PhotoImage(imagem_pil)
        rotulo = Label(root, image=self.imagem)
        rotulo.pack()

        self.container1 = Frame(root)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(root)
        self.container2["pady"] = 5
        self.container2["padx"] = 20
        self.container2.pack()

        self.container3 = Frame(root)
        self.container3["pady"] = 5
        self.container3["padx"] = 20
        self.container3.pack()

        self.container4 = Frame(root)
        self.container4["pady"] = 10
        self.container4["padx"] = 25
        self.container4.pack()

        self.titulo = Label(self.container1, text="CONVERSOR DE MOEDAS")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo["fg"] = "#E0BE12"
        self.titulo.pack()

        self.entryLabel = Label(self.container2,text="R$")
        self.entryLabel["font"] = ("Arial", "10", "bold")
        self.entryLabel.pack(side=LEFT)

        self.entry = Entry(self.container2)
        self.entry["width"] = 20
        self.entry["font"] = ("Arial", "10")
        self.entry.pack(side=LEFT)

        self.USD = Button(self.container3)
        self.USD["text"] = "Dólar (U$)"
        self.USD["font"] = ("Arial", "10", "bold")
        self.USD["width"] = 10
        self.USD["padx"] = 7
        self.USD["command"] = lambda: self.moedas("Dolar")
        self.USD.pack(side=LEFT, padx=(0, 10))

        self.EUR = Button(self.container3)
        self.EUR["text"] = "Euro (€)"
        self.EUR["font"] = ("Arial", "10", "bold")
        self.EUR["width"] = 10
        self.EUR["padx"] = 10
        self.EUR["command"] = lambda: self.moedas("Euro")
        self.EUR.pack(side=LEFT, padx=(0, 10))

        self.GPB = Button(self.container3)
        self.GPB["text"] = "Libra (£)"
        self.GPB["font"] = ("Arial", "10", "bold")
        self.GPB["width"] = 10
        self.GPB["padx"] = 10
        self.GPB["command"] = lambda: self.moedas("Libra")
        self.GPB.pack(side=LEFT)

    # Função para validar se o que foi escrito é um número
    def validarNum(self):
        valor = self.entry.get()
        valor = valor.replace(",", ".")  # Substitui vírgula por ponto
        if valor.isdigit():
            return True
        else:
            self.result("O valor que você inseriu é invaláido! Tente novamente.")

    def result(self, valor):
        if hasattr(self, 'resultLabel'):
            # Verifica se a label já foi criada, e se sim, atualiza o texto
            self.resultLabel.config(text=valor)
            self.resultLabel["font"] = ("Arial", 10, "bold")
        else:
            # Se a label ainda não existe, cria uma nova
            self.resultLabel = Label(self.container4, text=valor)
            self.resultLabel["font"] = ("Arial", 10, "bold")
            self.resultLabel.pack(side=LEFT)
    
    def moedas(self, moeda):
        resp = self.validarNum()
        
        if resp == True:
            valor = self.entry.get()
            valor = valor.replace(",", ".")

            # URL do endpoint da API Gateway para o GET
            get_url = 'http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,GBP-BRL'

            # Fazer a solicitação GET
            get_response = requests.get(get_url)

            # Extrair os dados do JSON
            jsonGet = get_response.json()
            if moeda == "Dolar":
                response = json.loads(jsonGet['USDBRL']['high'])
                resultado = float(valor) / float(response)
                resposta = (f"RESULTADO: R$ {resultado:.2f}")
                self.result(resposta)
            elif moeda == "Euro":
                response = json.loads(jsonGet['EURBRL']['high'])
                resultado = float(valor) / float(response)
                resposta = (f"RESULTADO: R$ {resultado:.2f}")
                self.result(resposta)     
            elif moeda == "Libra":
                response = json.loads(jsonGet['GBPBRL']['high'])
                resultado = float(valor) / float(response)
                resposta = (f"RESULTADO: R$ {resultado:.2f}")
                self.result(resposta)

# Inicia a interface
janela = Tk()
janela.title("Conversor de moedas")
ConversorMoedas(janela)
janela.mainloop()