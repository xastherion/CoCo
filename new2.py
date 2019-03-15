import tkinter as tk
from tkinter import *
import os

matrix = [
[0, '1-CMD_Name',   '3-Befehl'    ],
[1, 'auflisten',    'ls'          ],
[2, 'clear screen', 'clear'       ],
[3, 'erstellt file','touch test.txt'],
[4, '1-CMD_Name',   '3-Befehl'    ],
[5, 'auflisten',    'ls'          ],
[6, 'clear screen', 'clear'       ],
[7, 'erstellt file','touch test.txt']
]

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        text = tk.Text(self, wrap="none")
        vsb = tk.Scrollbar(orient="vertical", command=text.yview)
        text.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        text.pack(fill="both", expand=True)

        for element in matrix:
            leer_lista = StringVar(self, value=element[2])
            group = tk.LabelFrame(self, text=element[1], width=100, height=50, bg="grey")
            Entry(group, textvariable=leer_lista, width=80).pack(side=LEFT)
            Button(group, text='Do!', command=(lambda: os.system(leer_lista.get()))).pack(side=LEFT)
            text.window_create("end", window=group)
            text.window_create("end", window=group)
            text.insert("end", "\n")
        text.configure(state="disabled")

def ende():  # esta funcion terminatodo con el boton "Exit"
    master.destroy()

if __name__ == "__main__":
    master = tk.Tk()
    master.title('Commands_Container')
    master.geometry('810x600')  # breite-X-hohe x,y
    Example(master).pack(fill="both", expand=True)
    Button(master, text='Exit', command=ende).pack()
    master.mainloop()
