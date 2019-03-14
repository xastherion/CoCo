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
matrix = [
    [0,     '1-CMD_Name',   '2-Beschreibung',                                             '3-Befehl'],
    [1,     'auflisten',    'zeigt eine liste von alle dateien in aktuelle verzeichniss',   'ls'    ],
    [2,     'clear screen', 'lösch die sichbare bild',                                      'clear' ],
    [3,     'erstellt file','erstell eine Datei "test.txt" in das aktuelle Verzeichnis',    'touch test.txt']
        ]

#print(matrix[1][2])
#print((matrix))
cont = 0
largo = int(len(matrix))
#rango = int(range(matrix))
print("largo", largo)
#print("rango", rango)
for cont in np.nditer(matrix):
        #leer_lista = StringVar(master, value=lista_cmd[cont])
        print(cont)
        framex = Frame(master)

        group = LabelFrame(framex, text=(matrix[cont][1]), bg="blue")
        Label(group, text=(matrix[cont][2])).pack(side = TOP)
        Entry(group, textvariable=(matrix[cont][3]), width=100).pack(side = LEFT)
        Button(group, text='Do it!', command=lambda: os.system(leer_lista.get())).pack(side = LEFT)
        group.pack(side = LEFT)
        framex.pack()

#        w.pack(side = LEFT)

exit_button = Button(master, text='Exit', command=lambda : quit()).pack()
mainloop()