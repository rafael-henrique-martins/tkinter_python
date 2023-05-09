from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funcs():
    def limpar_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def conecta_db(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor(); print("conectando ao banco de dados clientes")
    def desconecta_db(self):
        self.conn.close(); print("banco de dados desconectado")
    def montaTabelas(self):
        self.conecta_db();
        ###criando tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
        );
        """)
        self.conn.commit(); print("banco de dados criado")
        self.desconecta_db()
    def add_cliente(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()

        self.conecta_db()
        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
        VALUES (?, ?, ?) """, (self.nome, self.telefone, self.cidade))
        self.conn.commit()

        self.desconecta_db()
        self.select_lista()
        self.limpar_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes ORDER BY nome_cliente ASC; """)

        for i in lista:
            self.listaCli.insert("", END, values=i)

        self.desconecta_db()

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.list_frame2()
        self.montaTabelas()
        self.select_lista()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastrar/excluir usuario do topico de SNS")
        self.root.configure(background= "#c0c0c0")
        self.root.geometry("780x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.minsize = self.root.minsize(width=500, height=400)
    def frames_da_tela(self):
        self.frames_1 = Frame(self.root, border=4, bg="#dfe3ee",
                              highlightbackground="#759fe6", highlightthickness=3)
        self.frames_1.place(relx= 0.02, rely=0.02, relwidth=0.96, relheight=0.46) # 0 = lado esquerdo/1 = lado direito da tela

        self.frames_2 = Frame(self.root, border=4, bg="#dfe3ee",
                              highlightbackground="#759fe6", highlightthickness=3)
        self.frames_2.place(relx= 0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self):
        # criando o botao de limpar
        self.bt_limpar = Button(self.frames_1, text="LIMPAR", bd=2, bg="#107db2",fg="#dfe3ee",font=("verdana",8,"bold"))
        self.bt_limpar.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # criando o botao de buscar
        self.bt_buscar = Button(self.frames_1, text="BUSCAR", bd=2, bg="#107db2",fg="#dfe3ee",font=("verdana",8,"bold"))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # criando o botao de novo
        self.bt_novo = Button(self.frames_1, text="NOVO", bd=2, bg="#107db2",fg="#dfe3ee",font=("verdana",8,"bold"),
                              command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # criando o botao de alterar
        self.bt_alterar = Button(self.frames_1, text="ALTERAR", bd=2, bg="#107db2",fg="#dfe3ee",font=("verdana",8,"bold"))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # criando o botao de apagar
        self.bt_apagar = Button(self.frames_1, text="APAGAR", bd=2, bg="#107db2",fg="#dfe3ee",font=("verdana",8,"bold"),
                                command=self.limpar_tela)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # criacao da label de entrada do codigo
        self.lb_codigo = Label(self.frames_1, text="Código", bg="#dfe3ee", fg="#107db2")
        self.lb_codigo.place(relx= 0.05, rely=0.05)

        self.codigo_entry = Entry(self.frames_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        # criacao da label de entrada do nome
        self.lb_nome = Label(self.frames_1, text="Nome", bg="#dfe3ee", fg="#107db2")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frames_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        # criacao da label de entrada do telefone
        self.lb_telefone = Label(self.frames_1, text="Telefone", bg="#dfe3ee", fg="#107db2")
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frames_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        # criacao da label de entrada do cidade
        self.lb_cidade = Label(self.frames_1, text="Cidade", bg="#dfe3ee", fg="#107db2")
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frames_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    def list_frame2(self):
        self.listaCli = ttk.Treeview(self.frames_2, height=3, columns=("col1","col2","col3","col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1,relwidth=0.95,relheight=0.85)

        self.scroolLista = Scrollbar(self.frames_2, orient="vertical")
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1,relwidth=0.04,relheight=0.85)

Application()