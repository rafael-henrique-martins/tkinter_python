from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funcs():
    def limpar_tela(self):
        self.topico_entry.delete(0, END)
        self.endpoint_entry.delete(0, END)
        self.protocolo_entry.delete(0, END)

    def variaveis(self):
        self.topico = self.topico_entry.get()
        self.endpoint = self.endpoint_entry.get()
        self.protocolo = self.protocolo_entry.get()

    def add_cliente(self):
        self.variaveis()

        self.limpar_tela()
    def select_lista(self, lista):
        self.listaCli.delete(*self.listaCli.get_children())

        for i in lista:
            self.listaCli.insert("", END, values=i)

    def buscar_topicos(self):
        lista_topicos = {'Topics': [{'TopicArn': "topicoeeeeeee-1"}, {'TopicArn': "topicoqqqqqq-2"}, {'TopicArn': "topico 3"}]}

        list_arn = []

        for i in lista_topicos['Topics']:
            list_arn.append(i['TopicArn'])

        self.select_lista(list_arn)

    def OnDoubleClick(self, event):
        self.limpar_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1 = self.listaCli.item(n, 'values')
            self.topico_entry.insert(END, col1)
            self.protocolo_entry.insert(END, "email")

    def deleta_cliente(self):
        self.variaveis()
        self.limpar_tela()

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.list_frame2()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastrar/excluir usuario do topico de SNS")
        self.root.configure(background= "#FFFACD")
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
        # criando o botao de LIMPAR
        self.bt_limpar = Button(self.frames_1, text="LIMPAR", bd=2, bg="#FFFAFA",fg="#107db2",font=("verdana",8,"bold"),
                                command=self.limpar_tela)
        self.bt_limpar.place(relx= 0.05, rely=0.75, relwidth=0.1, relheight=0.15)

        # criando o botao de BUSCAR
        self.bt_buscar = Button(self.frames_1, text="BUSCAR", bd=2, bg="#107db2",fg="#FFFAFA",font=("verdana",8,"bold"),
                                command=self.buscar_topicos)
        self.bt_buscar.place(relx=0.16, rely=0.75, relwidth=0.1, relheight=0.15)

        # criando o botao de ADICIONAR
        self.bt_novo = Button(self.frames_1, text="ADICIONAR", bd=2, bg="#32CD32",fg="#FFFAFA",font=("verdana",8,"bold"),
                              command=self.add_cliente)
        self.bt_novo.place(relx=0.67, rely=0.75, relwidth=0.12, relheight=0.15)

        # criando o botao de EXCLUIR
        self.bt_apagar = Button(self.frames_1, text="EXCLUIR", bd=2, bg="#FF6347",fg="#FFFAFA",font=("verdana",8,"bold"),
                                command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.75, relwidth=0.12, relheight=0.15)

        # criacao da label de entrada do topico
        self.lb_topico = Label(self.frames_1, text="Topico", bg="#dfe3ee", fg="#107db2",
                               font=("verdana",10,"bold"))
        self.lb_topico.place(relx=0.05, rely=0.1)

        self.topico_entry = Entry(self.frames_1)
        self.topico_entry.place(relx=0.05, rely=0.20, relwidth=0.8)

        # criacao da label de entrada do email
        self.lb_endpoint = Label(self.frames_1, text="Email", bg="#dfe3ee", fg="#107db2",
                                 font=("verdana",10,"bold"))
        self.lb_endpoint.place(relx=0.05, rely=0.35)

        self.endpoint_entry = Entry(self.frames_1)
        self.endpoint_entry.place(relx=0.05, rely=0.45, relwidth=0.4)

        # criacao da label de entrada do protocolo
        self.lb_protocolo = Label(self.frames_1, text="Protocolo", bg="#dfe3ee", fg="#107db2",
                                  font=("verdana",10,"bold"))
        self.lb_protocolo.place(relx=0.5, rely=0.35)

        self.protocolo_entry = Entry(self.frames_1)
        self.protocolo_entry.place(relx=0.5, rely=0.45, relwidth=0.25)
    def list_frame2(self):
        self.listaCli = ttk.Treeview(self.frames_2, height=3, columns=("col1"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Clique 2 vezes para selecionar o topico")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=700)


        self.listaCli.place(relx=0.01, rely=0.1,relwidth=0.95,relheight=0.85)

        self.scroolLista = Scrollbar(self.frames_2, orient="vertical")
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1,relwidth=0.04,relheight=0.85)

        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

Application()
