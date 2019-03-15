from tkinter import *
import os

master= Tk()
master.title('Commands_Container')
master.geometry('900x500') # breite-X-hohe x,y

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

def ende():  # esta funcion terminatodo con el boton "Exit"
    master.destroy()

def principal():
    framex = Frame(master)
    framex =        Frame(master)
    group =         LabelFrame(framex,  text=   element[1], width=100, bg="grey")
    leer_lista =    StringVar(master,   value=  element[2])
    Entry   (group, textvariable=leer_lista, width=80).pack(side=LEFT)
    Button  (group, text='Do!', command=(lambda: os.system(leer_lista.get()))).pack(side=LEFT)
    Label   (framex).pack() # Platzer
    group.pack()
    framex.pack()

for element in matrix:
    principal()

Label (master, text='').pack() # Platzer
Button(master, text='Exit', command=ende).pack()

master.mainloop()
