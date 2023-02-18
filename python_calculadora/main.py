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
def botao_adicao():
    return
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
#primeira fileira
def botao_click():
    return
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
adicao.grid(row=1, column=1)

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
adicao.grid(row=1, column=2)

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
adicao.grid(row=1, column=3)
root.mainloop()

