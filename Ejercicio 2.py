import numpy as np
class Matriz(object):
    def __init__(self, A, B):
        self.fil =""
        self.col =""
        self.false=False 
        ceros= np.zeros((A,B))
        print(ceros)
        
    def randon(self):
        array = np.random.randint(100, size=(A, B))
        print(array,"\n")
           
    def ranceros(self):
        self.false = input("              ¿Desea reiniciar la matriz?:\n\n"
                "Dijite: True;(Reiniciar)       Dijite: False;(Fin del Programa)\n")
        
        if self.false == "True" or  self.false == "true":
            
            c = np.zeros((A,B))
            print(c)
            print("                'Fin del Programa'")
        
        elif self.false =="False" or self.false == "false":
            print("                'Fin del Programa'")
            
            
A=int(input("Dijite Filas: "))
B=int(input("Dijite Columnas: "))
m= Matriz(A,B)
print("")
print(m.randon())
print(m.ranceros(),"\n")
    


        