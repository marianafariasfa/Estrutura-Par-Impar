import os

os.system("cls")

from tkinter import *

def verificar ():
    try:
        numero = int (entry_numero.get())
        
        if numero % 2 == 0:
            resultado_label.config(text=f"{numero} é Par!")

        else:
            resultado_label.config(text=f"{numero} é Impar!")
            
    except ValueError:
        resultado_label.config(text = "Por Favor, insira um número válido!")
        
cor1 = 'light yellow'

janela = Tk()
janela.title("Sistema Par ou Impar")
janela.geometry("400x300")
janela.config(bg=cor1)

titulo_label = Label (janela, text="Escolha um número Par ou Impar", font=("Arial", 13), bg = "light yellow", fg = "hot pink")
titulo_label.pack()

entrada_label = Label (janela, text= "\nDigite um número: ", font=("Arial", 13), bg = "light yellow", fg = "hot pink")
entrada_label.pack()

entry_numero = Entry(janela, font=("Arial", 13), bg = "white", fg = "black")
entry_numero.pack() 

verificar_btn = Button(janela, text="Verificar", font=("Arial", 13), command=verificar, bg = "light yellow", fg = "hot pink")
verificar_btn.pack(pady=10)

resultado_label = Label(janela, text="", font=("Arial", 13), bg = "light yellow", fg = "hot pink")
resultado_label.pack(pady=10)

janela.mainloop()