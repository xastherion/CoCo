#!/usr/local/bin/python3
# Python script for diferents configurations commands.
# Usage: Easy put your commands in the dictionary "lista_cmd"
# with a number. So you have your commands colecction. 
# If you need one to execute one of these commands, 
# you need only press the button "Do it!"
# if you need to edit some command for little variations and you dont
# want to save this variations, you can edit the command in the entry
# and then, press "Do it!" for this command

# TODO´s : a comments place on window (not here in script)

import os
from tkinter import *

master = Tk()
master.title('Commands_Container')
master.geometry('500x500') # breite-X-hohe x,y
# ---------------- List of Defaults commands ----------------------
lista_cmd = {
    0:'----- MUNKI-CLIENT CONFIGURATION',
    4:'ls',
    5:'clear',
    6:'touch test.txt',
}

for cont in lista_cmd:
        leer_lista = StringVar(master, value=lista_cmd[cont])
        framex = Frame(master)

        group = LabelFrame(framex, text=leer_lista.get(), bg="blue")
        Label(group, text=leer_lista.get()).pack()
        Entry(group, textvariable=leer_lista, width=100).pack()
        Button(group, text='Do it!', command=lambda: os.system(leer_lista.get())).pack()
        group.pack()
        framex.pack()

#        w.pack(side = LEFT)

exit_button = Button(master, text='Exit', command=lambda : quit()).pack()
mainloop()