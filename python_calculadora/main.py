from tkinter import *

root = Tk()
root.title('CALCULADORA')
root.geometry('480x360')
root.minsize(480,360)
root.maxsize(480,360)

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28f', 
font=('futura', 25, 'bold'), justify=CENTER,)
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
root.mainloop()

