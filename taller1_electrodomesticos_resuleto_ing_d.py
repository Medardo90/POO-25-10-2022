# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:54:18 2022

@author: Patricio Haro
"""
# Para importar la biblioteca random al completo
import random
from random import choice

class Electrodomestico:
    coloresAdm= ['blanco', 'rojo', 'azul']
    consumosAdm=['A','B','C']
    
    def __init__(self,peso,consumo,color=None,precioBase=None):
        if color is None:
            color=random.choice(self.coloresAdm)
        
        self.consumo=consumo
        self.color= color
        self.consumo=consumo
        self.peso=peso
        
        if precioBase is None:
            if consumo == 'A':
                precioBase=100
            elif consumo == 'B':
                precioBase=80
            else:
                precioBase=60
            
        self.precioBase = precioBase
        
class  Lavadora(Electrodomestico):
    
    def __init__(self,peso,consumo,carga,color=None,precioBase=None):
        Electrodomestico.__init__(self,peso,consumo,color=None,precioBase=None)
        
        self.carga = carga
        
        if carga >0 and carga <20:
            self.precioBase=(1+0.1)*self.precioBase
           
        elif carga >=20 and carga <50:
            self.precioBase=(1+0.2)*self.precioBase
            
        elif carga >=50 and carga <80:
            self.precioBase=(1+0.3)*self.precioBase
            
        elif carga >=80:
            self.precioBase=(1+0.4)*self.precioBase
            

class TiendaElectrodomesticos:
    Lav1=Lavadora(10,'A',10) #(Peso,consumo,carga)
    Lav2=Lavadora(20,'A',25) #(Peso,consumo,carga)
    Lav3=Lavadora(30,'B',30) #(Peso,consumo,carga)
    Lav4=Lavadora(40,'B',45) #(Peso,consumo,carga)
    Lav5=Lavadora(50,'C',60) #(Peso,consumo,carga)
    Lav6=Lavadora(60,'C',75) #(Peso,consumo,carga)
    Lav7=Lavadora(70,'A',90) #(Peso,consumo,carga)
    Lav8=Lavadora(80,'A',100) #(Peso,consumo,carga)
    
    def preciosTotalesStock(self):
        total=self.Lav1.precioBase+self.Lav2.precioBase+self.Lav3.precioBase+self.Lav4.precioBase+self.Lav5.precioBase+self.Lav6.precioBase+self.Lav7.precioBase+self.Lav8.precioBase
        
        print(" ------------Precios Totales------------")
        print("L1 -  $"+'%.2f' %self.Lav1.precioBase+"\n")
        print("L2 -  $"+'%.2f' %self.Lav2.precioBase+"\n")
        print("L3 -  $"+'%.2f' %self.Lav3.precioBase+"\n")
        print("L4 -  $"+'%.2f' %self.Lav4.precioBase+"\n")
        print("L5 -  $"+'%.2f' %self.Lav5.precioBase+"\n")
        print("L6 -  $"+'%.2f' %self.Lav6.precioBase+"\n")
        print("L7 -  $"+'%.2f' %self.Lav7.precioBase+"\n")
        print("L8 -  $"+'%.2f' %self.Lav8.precioBase+"\n")
        print("\n TOTAL -  $"+'%.2f' %total+"\n")
    
'''Programa'''
Tienda1=TiendaElectrodomesticos()
Tienda1.preciosTotalesStock()
