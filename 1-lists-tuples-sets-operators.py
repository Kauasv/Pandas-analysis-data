import tkinter as tk
from tkinter import scrolledtext

# Função que exibe a saída do código
def mostrar_saida():
    saida = """
------------------------
Lista de coleçao ordenada e mutavel
------------------------
lista de numeros  []
lista de letras  []
lista de mistura  []

------------------------
adicionando e modificando itens na lista
------------------------
Lista alterada [99]

------------------------
#Tuplas
------------------------
tupla:  ('what', 'who', 'where')

------------------------
#um set é uma coleção não ordenada e não permite itens duplicados
------------------------
set sem duplicatas {'banana', 'laranja', 'maça'}
set apos add : {'banana', 'laranja', 'maça'}

------------------------
Fozen set
------------------------
frozenset : frozenset({'batata', 'alface', 'uva'})

------------------------
Operação entre setas 
------------------------
uniao de a com b : {1, 2, 3, 4, 5}
interseçãqo : {3}
diferença {1, 2}

------------------------
operadores
------------------------
x= 10 y= 5
x igualdade y False
x diferente y  True
x mairo que y  True
x menor que y  False
x menor ou igual que y False
x maior ou igual que y True
------------------------
Operadores aritméticos
------------------------
soma = 7
Subtração = 3
multiplicação = 10
divisão = 2.5
Divisão inteira = 2
resto da divisão = 1
potencia = 25
------------------------
Operadores lógicos
------------------------
p and q: False
p or q: True
not p: False
------------------------
"""
    # Limpar e inserir o texto na área
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, saida)

# Criar janela principal
janela = tk.Tk()
janela.title("Saída do Código Python")
janela.geometry("700x500")

# Botão para mostrar a saída
botao = tk.Button(janela, text="Mostrar Saída", command=mostrar_saida)
botao.pack(pady=10)

# Caixa de texto rolável
text_area = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=80, height=25)
text_area.pack(padx=10, pady=10)

# Executar a janela
janela.mainloop()
