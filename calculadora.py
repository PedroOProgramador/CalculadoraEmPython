import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")

#executa os calculos
def executar():
    global coleta
    resultado = eval(coleta)
    texto.config(text=resultado)

#0 até o * é só para escrever

def escreva1():
    global coleta
    coleta += '1'
    texto.config(text=coleta)

def escreva2():
    global coleta
    coleta += '2'
    texto.config(text=coleta)

def escreva3():
    global coleta
    coleta += '3'
    texto.config(text=coleta)

def escreva4():
    global coleta
    coleta += '4'
    texto.config(text=coleta)

def escreva5():
    global coleta
    coleta += '5'
    texto.config(text=coleta)

def escreva6():
    global coleta
    coleta += '6'
    texto.config(text=coleta)

def escreva7():
    global coleta
    coleta += '7'
    texto.config(text=coleta)

def escreva8():
    global coleta
    coleta += '8'
    texto.config(text=coleta)

def escreva9():
    global coleta
    coleta += '9'
    texto.config(text=coleta)

def escrevaMais():
    global coleta
    coleta += '+'
    texto.config(text=coleta)

def escrevaMenos():
    global coleta
    coleta += '-'
    texto.config(text=coleta)

def escrevaDivisao():
    global coleta
    coleta += '/'
    texto.config(text=coleta)

def escrevaMultiplicacao():
    global coleta
    coleta += '*'
    texto.config(text=coleta)

def escreva0():
    global coleta
    coleta += '0'
    texto.config(text=coleta)

#Cria os botoes e a tela
global texto 
coleta = ''


texto = tk.Label(janela,text="Teste",padx=25,pady=20)
texto.grid(row=0,column=0)



tk.Button(janela,text="executar",padx=20,command=executar).grid(row=0,column=1,columnspan=2)
tk.Button(janela,text="1",padx=20,pady=20,command=escreva1).grid(row=1,column=0)
tk.Button(janela,text="2",padx=20,pady=20,command=escreva2).grid(row=1,column=1)
tk.Button(janela,text="3",padx=20,pady=20,command=escreva3).grid(row=1,column=2)
tk.Button(janela,text="4",padx=20,pady=20,command=escreva4).grid(row=2,column=0)
tk.Button(janela,text="5",padx=20,pady=20,command=escreva5).grid(row=2,column=1)
tk.Button(janela,text="6",padx=20,pady=20,command=escreva6).grid(row=2,column=2)
tk.Button(janela,text="7",padx=20,pady=20,command=escreva7).grid(row=3,column=0)
tk.Button(janela,text="8",padx=20,pady=20,command=escreva8).grid(row=3,column=1)
tk.Button(janela,text="9",padx=20,pady=20,command=escreva9).grid(row=3,column=2)
tk.Button(janela,text="0",padx=20,pady=20,command=escreva0).grid(row=4,column=0)
tk.Button(janela,text="+",padx=20,pady=20,command=escrevaMais).grid(row=4,column=1)
tk.Button(janela,text="-",padx=20,pady=20,command=escrevaMenos).grid(row=4,column=2)
tk.Button(janela,text="/",padx=20,pady=20,command=escrevaDivisao).grid(row=5,column=0)
tk.Button(janela,text="*",padx=20,pady=20,command=escrevaMultiplicacao).grid(row=5,column=1)


janela.mainloop()