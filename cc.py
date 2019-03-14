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
from subprocess import Popen

mGui = Tk()

# ---------------- List of Defaults commands ----------------------
lista_cmd = {
# ------- MUNKI
    0:'----- MUNKI-CLIENT CONFIGURATION',
    4:'ls',
    5:'clear',
    6:'touch test.txt',
}
# ================ End Defaults Commands ===========================

# ---------------- Dialog Boxes building ---------------------------
for cont in lista_cmd:
    def command_01():
        leer_lista = StringVar(mGui, value=lista_cmd[cont])
        framex = Frame(mGui)
        Entry(framex, textvariable=leer_lista, width=170).pack(side=LEFT)
        Button(framex, text='Do it!', command=lambda: os.system(leer_lista.get())).pack(side=RIGHT)
        framex.pack()

    command_01()
# ================ End Dialog Boxes building =======================

# ---- Building Exit Button ------
exit_button = Button(mGui, text='Exit', command=lambda : quit()).pack()
mainloop()
