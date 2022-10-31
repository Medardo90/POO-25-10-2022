# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:10:01 2022

@author: lab
"""

"""primer metosdo todo el programa en un solo archivo"""
#if name se nesecita para llamar osea es principal 

class Model_Operations():
    def __init__(self):
        print("                      Estoy en el MODEl\n")
        print("                Desea realizar alguna operacion?\n")
        print("Digite 1: (suma)               Digite 2: (resta)\n"
              "Digite 3: (multiplicacion)     Digite 4: (division) ")
        
        
    def suma(self,var1,var2):      # resultado= var1+var2
                                   # return resultado
        return var1+var2          
       
    def resta(self,var1, var2):
        return var1-var2
    
    def multiplicacion(self,var1, var2):
        return var1*var2
    
    def division(self,var1, var2):
       return var1/var2
#####################################################            
class View_Operations():
    def __init__(self,model):
        self.model = model
        
    def inputData(self):
        self.var1= eval(input("Ingerese un numero: "))
        return  self.var1
    
    def showOperations(self):
        var1Vlew=self.inputData()
        var2Vlew=self.inputData()
        print("el resultado de la suma es: ", self.model.suma(var1Vlew,var2Vlew))
        print("el resultado de la resta es : ", self.model.resta(var1Vlew,var2Vlew))
        print("el resultado de la multiplicacion es : ", self.model.multiplicacion(var1Vlew,var2Vlew))
        print("el resultado de la division  es : ", self.model.division(var1Vlew,var2Vlew))
##############################################################    
class Controller_Operations():
    def __init__(self,model,view):
        self.model=model
        self.view=view

    def runOperation(self):
        self.view.showOperations()
#####################################################
if __name__ == "__main__":
    model=Model_Operations()
    view=View_Operations(model)
    c= Controller_Operations(model,view)
    c.runOperation()

