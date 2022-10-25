# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:15:24 2022

@author: lab
"""

class Rueda:
    def __init__(self, color,marca):
        self.color= color
        self.marca =marca 

class Vehiculo:
    def __init__(self,numruedas):
        self.numruedas= numruedas
        
    def incorporarrueda(self):
        ruedas=[]
        ruedas.append(Rueda("negra","amarilla"))
        ruedas.append(Rueda("roja","continetal"))
        ruedas.append(Rueda("amarilla","gy"))
        ruedas.append(Rueda("roja","hamkot"))
     
        
        return  ruedas
    
    def generarRuedas(self):
        ruedas=[]
        for i in range(0, self.numruedas):
            ruedas.append(Rueda("negra","millelin"))
        return  ruedas
    
obj_vehiculo = Vehiculo(10)
ruedas = obj_vehiculo.generarRuedas()
for i in ruedas:
    print(i.marca)