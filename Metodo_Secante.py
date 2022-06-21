from cProfile import label
from operator import index
from tkinter import *
from tkinter import ttk

import math
from tkinter.tix import MAX
#10*x**4-5*x**3-3*x**2+2*x+5
#x**3-math.sin(x)+4
#20*x**3-math.cos(x)+10

janela = Tk()

class Funcs():
    #Limpar Botões da Primeira Tela
    def limpa_tela(self):
        self.entry_equacao.delete(0,END)
        self.entry_valx0.delete(0,END)
        self.entry_valx1.delete(0,END)
        self.entry_epsilon.delete(0,END)
        self.entry_valmax.delete(0,END)
        self.listaSecante.drop()

    #Iniciar o Calculo do Metodo
    def valor_calcular(self):
        self.valorx0=eval(self.entry_valx0.get())
        self.valorx1=eval(self.entry_valx1.get())
        self.epsilon=eval(self.entry_epsilon.get())
        self.valmax=eval(self.entry_valmax.get())
        def SecanteMeto(x0, x1, valmax, epsilon):
            # Ferifica máximo de Iteração
            if (valmax <= 0):
                return x1

            # calcula secante
            fx0 = fun_equacao_x(x0)
            funcx0=fx0
            fx1 = fun_equacao_x(x1)
            secante = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
            fx0 = fun_equacao_x(secante)

            # imprime Tabela
            elementos= [f"{funcx0:>10f}",f"{fx1:>10f}",f"{fx0:>10f}",f"{secante:>10f}"]
            self.listaSecante.insert("", END, values=elementos, tag='1')
            # Verifica se chegou na tolerancia aceitavel
            if (abs(fx0) <= epsilon):
                #self.textos = StringVar()
                #self.textos= [f"\nResultado: {secante:>9f}\n\n"]
                print(f"\nResultado: {secante:>9f}\n\n")
            else:
                SecanteMeto(x1, secante, valmax - 1, epsilon)

        def fun_equacao_x(x):
            return eval(self.entry_equacao.get().replace('x', str(x)))

        SecanteMeto(self.valorx0,self.valorx1,self.valmax,self.epsilon)
    

class aplicacao(Funcs):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.widgets_frames1()
        self.tables_frame2()
        janela.mainloop()
    def tela(self):
        self.janela.title("METODO DA SECANTE")
        self.janela.configure(background= '#708090')
        self.janela.geometry("850x550")
        self.janela.resizable(True, True)
        self.janela.maxsize(width= 880, height= 680)
        self.janela.minsize(width=550, height=380)
        #Telas
    def frames(self):
        self.frame1 = Frame(self.janela, bd = 4, bg = '#dedcdc',
                            highlightbackground= 'black', highlightthickness=3 )
        self.frame1.place(relx= 0.02 , rely=0.02, relwidth= 0.96,relheight= 0.45)

        self.frame2 = Frame(self.janela, bd=4, bg='#dedcdc',
                            highlightbackground='black', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)
    def widgets_frames1(self):
        #Botão Iniciar Calculo do Metodo#
        self.bt_limpar = Button(self.frame1, text="Calcular", bd= 2, bg="#006eff", command= self.valor_calcular)
        self.bt_limpar.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.15)
        #Botão Apagar tudo#
        self.bt_limpar = Button(self.frame1, text="Limpar", bd= 2, bg="#f20c0c",command=self.limpa_tela)
        self.bt_limpar.place(relx=0.65, rely=0.8, relwidth=0.1, relheight=0.15)

        #Label da Equação digitada
        self.lb_equacao= Label(self.frame1, text="Digite a Equação:", bd = 4, bg = '#dedcdc')
        self.lb_equacao.place(relx=0.05, rely=0.2)
        #Label Intervalo de X0
        self.lb_intx0= Label(self.frame1, text="Valor de X0:", bd = 4, bg = '#dedcdc')
        self.lb_intx0.place(relx=0.4, rely=0.2)
        #Label Intervalo de X1
        self.lb_intx1= Label(self.frame1, text="Valor de X1:", bd = 4, bg = '#dedcdc')
        self.lb_intx1.place(relx=0.6, rely=0.2)
        #Label Epsilon
        self.lb_epsilon= Label(self.frame1, text="Epsilon:", bd = 4, bg = '#dedcdc')
        self.lb_epsilon.place(relx=0.8, rely=0.2)
        #Label Valor Maximo de Interaçoes
        self.lb_valmax= Label(self.frame1, text="Quantidade de Interacoes:", bd = 4, bg = '#dedcdc')
        self.lb_valmax.place(relx=0.05, rely=0.6)

        #Entrada Valor da Equação
        self.entry_equacao= Entry(self.frame1)
        self.entry_equacao.place(relx=0.05, rely=0.3,relwidth=0.3, relheight=0.15)
        #Entrada Valor x0
        self.entry_valx0= Entry(self.frame1)
        self.entry_valx0.place(relx=0.4, rely=0.3,relwidth=0.1, relheight=0.15)
        #Entrada Valor x1
        self.entry_valx1= Entry(self.frame1)
        self.entry_valx1.place(relx=0.6, rely=0.3,relwidth=0.1, relheight=0.15)
        #Entrada Valor epsilon 
        self.entry_epsilon= Entry(self.frame1)
        self.entry_epsilon.place(relx=0.8, rely=0.3,relwidth=0.1, relheight=0.15)
        #Entrada Valor Maximo de Interaçoes
        self.entry_valmax= Entry(self.frame1)
        self.entry_valmax.place(relx=0.05, rely=0.7,relwidth=0.1, relheight=0.15)

    def tables_frame2(self):
        self.listaSecante= ttk.Treeview(self.frame2, height=3, column=("column1","column2","column3","column4"))
        #Posição das Colunas
        self.listaSecante.heading("#0", text="")
        self.listaSecante.heading("#1", text="f(x0)")
        self.listaSecante.heading("#2", text="f(x1)")
        self.listaSecante.heading("#3", text="f(x)")
        self.listaSecante.heading("#4", text="Secante")
        #Tamanhao da largura coluna
        self.listaSecante.column("#0", width=0)
        self.listaSecante.column("#1", width=100)
        self.listaSecante.column("#2", width=100)
        self.listaSecante.column("#3", width=100)
        self.listaSecante.column("#4", width=100)
        self.listaSecante.place(relx=0.01, rely=0.1,relwidth=0.95, relheight=0.85)
        #Barra de Rolagem
        self.scroolSecante= ttk.Scrollbar(self.frame2, orient='vertical',command=self.listaSecante.yview)
        self.scroolSecante.place(relx=0.96, rely=0.1,relwidth=0.02, relheight=0.85)
        self.listaSecante['yscrollcommand'] = self.scroolSecante.set


aplicacao()