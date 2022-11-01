# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:14:55 2022

@author: lab
"""

import tkinter

raiz =tkinter.Tk()
raiz.title("POO-UPS")
boton = tkinter.Button(raiz,text= "Aceptar",background = "green")
etiqueta= tkinter.Label(raiz,text="hola mundo")


boton.pack() # pack es apilar 
etiqueta.pack()
raiz.mainloop()





