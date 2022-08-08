"""
Utilizamos neste código a biblioteca tkinter.
"""
from tkinter import *
from tkinter import messagebox

def somar():
    """
    A função realiza operações de adição, e retorna o resultado na tela.
    """
    numero1 = float(caixa_editavel_1.get())
    numero2 = float(caixa_editavel_2.get())

    resultado = numero1 + numero2

    text = Label(interface_1, text="+  ", bg="#0C0C0C", font=("Arial", 30, "bold"), fg="#FFFFFF", cursor="hand2")
    text.place(x=210, y=55)

    text = Label(interface_1, text=("{0:,.2f}     ".format(resultado)), bg="#0C0C0C", font=("Arial", 50, "bold"), fg="#FFFFFF", cursor="hand2")
    text.place(x=150, y=150)
    
def subtrair():
    """
    A função realiza operações de subtração, e retorna o resultado na tela.
    """
    numero1 = float(caixa_editavel_1.get())
    numero2 = float(caixa_editavel_2.get())

    resultado = numero1 - numero2
    
    text = Label(interface_1, text="-   ", bg="#0C0C0C", font=("Arial", 30, "bold"), fg="#FFFFFF", cursor="hand2")
    text.place(x=210, y=55)

    text = Label(interface_1, text=("{0:,.2f}     ".format(resultado)), bg="#0C0C0C", font=("Arial", 50, "bold"), fg="#FFFFFF", cursor="hand2")
    text.place(x=150, y=150)
    
def multiplicar():
    """
    Função realiza operação de multiplicação, e retorna o resultado na tela.
    """

    numero1 = float(caixa_editavel_1.get())
    numero2 = float(caixa_editavel_2.get())

    resultado = numero1 * numero2
    
    text = Label(interface_1, text="x", bg="#0C0C0C", font=("Arial", 30, "bold"), fg="#FFFFFF", cursor="hand2")
    text.place(x=210, y=55)

    text = Label(interface_1, text=("{0:,.2f}       ".format(resultado)), bg="#0C0C0C", font=("Arial", 50, "bold"), fg="#FFFFFF", cursor="hand2")
    text.place(x=150, y=150)
    
def dividir():
    """
    Função realiza operação de divisão, e retorna o resultado na tela.
    """

    numero1 = float(caixa_editavel_1.get())
    numero2 = float(caixa_editavel_2.get())

    resultado = numero1 / numero2
    
    text = Label(interface_1, text="÷", bg="#0C0C0C", font=("Arial", 30, "bold"), fg="#FFFFFF", cursor="hand2")
    text.place(x=210, y=55)
  
    text = Label(interface_1, text=("{0:,.2f}      ".format(resultado)), bg="#0C0C0C", font=("Arial", 50, "bold"), fg="#FFFFFF", cursor="hand2")
    text.place(x=150, y=150)
    
def porcentagem():
    """
    Função realiza operação de porcentagem, e retorna o resultado na tela.
    """

    numero1 = float(caixa_editavel_1.get())
    numero2 = float(caixa_editavel_2.get())

    div = float(100)
    resultado = (numero1 * numero2 / div)

    text = Label(interface_1, text="%", bg="#0C0C0C", font=("Arial", 30, "bold"), fg="#FFFFFF", cursor="hand2")
    text.place(x=210, y=55)

    text = Label(interface_1, text=("{0:,.2f}      ".format(resultado)), bg="#0C0C0C", font=("Arial", 50, "bold"), fg="#FFFFFF", cursor="hand2")
    text.place(x=150, y=150)
    
def finalizar():
    """
    Função mostra uma mensagem na tela, e tem função de destruir a janela.
    """
    if messagebox.askokcancel("Encerrando...", "Tem certeza que deseja sair?"):
        interface_1.destroy()

def sair(event):
    """
    Chama a função finalizar.
    """
    finalizar()

"""
A seguir, primeiro criamos a janela interface_1 e adicionamos os dados das informações da janela
a dimensão, icone, título e cor.
"""
interface_1 = Tk()
interface_1.geometry("444x350")
interface_1.resizable(0,0)
interface_1.title("Calculadora")
interface_1.configure(background='#0C0C0C')

"""
Textos que são exibidos ao criar a janela.
"""
text = Label(interface_1, text="C A L C U L A D O R A", bg="#0C0C0C", font=("Arial", 20, "bold"), fg="#FFFFFF", cursor="hand2")
text.place(x=70, y=5)

text = Label(interface_1, text="_______________________", bg="#0C0C0C", font=("Arial", 20, "bold"), fg="#FFFFFF", cursor="hand2")
text.place(x=50, y=90)

"""
Caixas editáveis para que os dados do usuário sejam adicionados.
"""
caixa_editavel_1 = StringVar()
caixa_editavel_1Box = Entry(interface_1, font=("Arial", 30, "bold"), textvariable=caixa_editavel_1)
caixa_editavel_1Box.place(x= 65, y=55, width=100, height=50)

caixa_editavel_2 = StringVar()
caixa_editavel_2Box = Entry(interface_1, font=("Arial", 30, "bold"), textvariable=caixa_editavel_2)
caixa_editavel_2Box.place(x= 280, y=55, width=100, height=50)

"""
Os botões a seguir são responsáveis pelas operações matemáticas e estão vinculados
as funções somar, subtrair, multiplicar, dividir, porcentagem e sair.
"""
botao_1 = Button(interface_1, text="+", font=("Arial", 20, "bold"), command=somar)
botao_1.config(height=1, width=4)
botao_1.place(x=10, y=250)

botao_2 = Button(interface_1, text="-", font=("Arial", 20, "bold"), command=subtrair)
botao_2.config(height=1, width=4)
botao_2.place(x=96, y=250)

botao_3 = Button(interface_1, text="x", font=("Arial", 20, "bold"), command=multiplicar)
botao_3.config(height=1, width=4)
botao_3.place(x=182, y=250)

botao_4 = Button(interface_1, text="÷", font=("Arial", 20, "bold"), command=dividir)
botao_4.config(height=1, width=4)
botao_4.place(x=268, y=250)

botao_5 = Button(interface_1, text="%", font=("Arial", 20, "bold"), command=porcentagem)
botao_5.config(height=1, width=4)
botao_5.place(x=354, y=250)

botao_6 = Button(interface_1, text="SAIR", command="sair")
botao_6.bind("<Button-1>", sair)
botao_6.config(height=1, width=5)
botao_6.place(x=197, y=315)    
    
interface_1.mainloop()