from tkinter import *

root = Tk()
root.title('CALCULADORA')
root.geometry('480x360')
root.minsize(480,360)
root.maxsize(480,360)

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28f', 
font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)
#function operation
def botao_click():
    return
def botao_adicao():
    return
def botao_subtracao():
    return
def botao_multiplicacao():
    return
def botao_divisao():
    return
def botao_limpar():
    return
def botao_igual():
    return
#botoes de operacoes
adicao = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_adicao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240086',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
adicao.grid(row=0, column=4)
subtracao = Button(root,
                text='-',
                padx=40,
                pady=20,
                command=botao_subtracao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240086',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
subtracao.grid(row=1, column=4)
multiplicacao = Button(root,
                text='*',
                padx=40,
                pady=20,
                command=botao_multiplicacao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240086',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
multiplicacao.grid(row=2, column=4)
divisao = Button(root,
                text='/',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240086',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
divisao.grid(row=3, column=4)
#primeira fileira
um = Button(root,
            text='1',
            padx=40,
            pady=20,
            command=lambda: botao_click(1),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
um.grid(row=1, column=1)

dois = Button(root,
            text='2',
            padx=40,
            pady=20,
            command=lambda: botao_click(2),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
dois.grid(row=1, column=2)

tres = Button(root,
            text='3',
            padx=40,
            pady=20,
            command=lambda: botao_click(3),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
tres.grid(row=1, column=3)

#segunda fileira
quatro = Button(root,
            text='4',
            padx=40,
            pady=20,
            command=lambda: botao_click(4),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
quatro.grid(row=2, column=1)

cinco = Button(root,
            text='5',
            padx=40,
            pady=20,
            command=lambda: botao_click(5),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
cinco.grid(row=2, column=2)

seis = Button(root,
            text='6',
            padx=40,
            pady=20,
            command=lambda: botao_click(6),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
seis.grid(row=2, column=3)
#terceira fileira
sete = Button(root,
            text='7',
            padx=50,
            pady=20,
            command=lambda: botao_click(7),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
sete.grid(row=3, column=1)
oito = Button(root,
            text='8',
            padx=50,
            pady=20,
            command=lambda: botao_click(8),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
oito.grid(row=3, column=2)
nove = Button(root,
            text='9',
            padx=50,
            pady=20,
            command=lambda: botao_click(9),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
nove.grid(row=3, column=3)
#quarta fileira
zero = Button(root,
            text='0',
            padx=110,
            pady=20,
            command=lambda: botao_click(0),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
zero.grid(row=4, column=1, columnspan=2)
apagar = Button(root,
            text='C',
            padx=50,
            pady=20,
            command=botao_limpar,
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
apagar.grid(row=4, column=3)
igual = Button(root,
            text='=',
            padx=50,
            pady=20,
            command=botao_igual,
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240086',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
igual.grid(row=4, column=4)

root.mainloop()

