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
from os import *

master = Tk()
master.title('Commands_Container')
master.geometry('500x500') # breite-X-hohe x,y
# ---------------- List of Defaults commands ----------------------
matrix = [
    [0,     '1-CMD_Name',   '2-Beschreibung',                                             '3-Befehl'],
    [1,     'auflisten',    'zeigt eine liste von alle dateien in aktuelle verzeichniss',   'ls'    ],
    [2,     'clear screen', 'lösch die sichbare bild',                                      'clear' ],
    [3,     'erstellt file','erstell eine Datei "test.txt" in das aktuelle Verzeichnis',    'touch test.txt']
        ]

for cont in matrix:
        framex = Frame(master)
        group = LabelFrame(framex, text=cont[1], bg="grey")
        leer_lista = StringVar(master, value=cont[3])
        print(leer_lista.get())
        command = leer_lista.get()
        Label(group, text=cont[2]).pack()
        Entry(group, textvariable=leer_lista, width=100).pack()
        Button(group, text='Do it!', command=lambda: os.system(command)).pack()
        group.pack(side = LEFT)
        framex.pack()

exit_button = Button(master, text='Exit', command=lambda : quit()).pack()
mainloop()