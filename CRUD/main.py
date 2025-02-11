# Importando o Tkinter e módulos necessários
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Tentando importar a view.py
try:
    from view import *
except ImportError:
    messagebox.showerror("Erro", "O arquivo 'view.py' não foi encontrado ou contém erros.")

################# Cores #################
co0 = "#f0f3f5"  # Cinza claro
co1 = "#feffff"  # Branco
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Azul escuro
co4 = "#403d3d"  # Cinza escuro
co5 = "#e06636"  # Laranja
co6 = "#038cfc"  # Azul
co7 = "#ef5350"  # Vermelho
co8 = "#263238"  # Verde escuro
co9 = "#e9edf5"  # Azul claro

################### Criando Janela ###################
janela = Tk()
janela.title("Sistema de Consultoria")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(False, False)  # Janela fixa

################# Criando Frames #################
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

################## Label Título #################
app_nome = Label(frame_cima, text='Formulário de Consultoria', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

# Variável global para a tabela
global tree

################# Funções CRUD #################

def inserir():
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    dia = e_cal.get()
    estado = e_estado.get()
    sobre = e_sob.get()

    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
        lista = [nome, email, tel, dia, estado, sobre]
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        limpar_campos()
        atualizar_tabela()

def atualizar():
    try:
        selected_item = tree.selection()[0]
        valores = tree.item(selected_item, 'values')

        if not valores:
            messagebox.showerror('Erro', 'Nenhum item selecionado.')
            return

        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_tel.delete(0, END)
        e_cal.set_date(valores[4])
        e_estado.delete(0, END)
        e_sob.delete(0, END)

        e_nome.insert(0, valores[1])
        e_email.insert(0, valores[2])
        e_tel.insert(0, valores[3])
        e_estado.insert(0, valores[5])
        e_sob.insert(0, valores[6])

        def confirmar_atualizacao():
            lista = [valores[0], e_nome.get(), e_email.get(), e_tel.get(), e_cal.get(), e_estado.get(), e_sob.get()]
            atualizar_info(lista)
            messagebox.showinfo('Sucesso', 'Dados atualizados com sucesso')
            limpar_campos()
            atualizar_tabela()

        b_confirmar = Button(frame_baixo, text='Confirmar', width=10, command=confirmar_atualizacao, font=('Ivy 9 bold'), bg=co2, fg=co1)
        b_confirmar.place(x=110, y=370)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item da tabela.')

def deletar():
    try:
        selected_item = tree.selection()[0]
        valor_id = [tree.item(selected_item, 'values')[0]]
        deletar_info(valor_id)
        messagebox.showinfo('Sucesso', 'Dados deletados')
        atualizar_tabela()
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item para deletar.')

def limpar_campos():
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    e_estado.delete(0, END)
    e_sob.delete(0, END)

def atualizar_tabela():
    for widget in frame_direita.winfo_children():
        widget.destroy()
    mostrar()

################## Campos de Entrada #################
Label(frame_baixo, text='Nome*', bg=co1).place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45)
e_nome.place(x=10, y=40)

Label(frame_baixo, text='Email*', bg=co1).place(x=10, y=70)
e_email = Entry(frame_baixo, width=45)
e_email.place(x=10, y=100)

Label(frame_baixo, text='Telefone*', bg=co1).place(x=10, y=130)
e_tel = Entry(frame_baixo, width=45)
e_tel.place(x=10, y=160)

Label(frame_baixo, text='Data da Consulta*', bg=co1).place(x=10, y=190)
e_cal = DateEntry(frame_baixo, width=12)
e_cal.place(x=10, y=220)

Label(frame_baixo, text='Estado*', bg=co1).place(x=160, y=190)
e_estado = Entry(frame_baixo, width=20)
e_estado.place(x=160, y=220)

Label(frame_baixo, text='Sobre*', bg=co1).place(x=10, y=260)
e_sob = Entry(frame_baixo, width=45)
e_sob.place(x=10, y=290)

################## Botões #################
Button(frame_baixo, text='Inserir', width=10, command=inserir, bg=co6, fg=co1).place(x=10, y=340)
Button(frame_baixo, text='Atualizar', width=10, command=atualizar, bg=co2, fg=co1).place(x=110, y=340)
Button(frame_baixo, text='Deletar', width=10, command=deletar, bg=co7, fg=co1).place(x=200, y=340)

################## Tabela #################
def mostrar():
    global tree
    lista = mostrar_info()

    colunas = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'Estado', 'Sobre']
    tree = ttk.Treeview(frame_direita, columns=colunas, show="headings")

    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for item in lista:
        tree.insert("", "end", values=item)

    tree.pack(expand=True, fill="both")

mostrar()

janela.mainloop()
