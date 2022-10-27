salval=0
salval2=0
retiro=0
retiro2=0
def validacion(valor):
    while True:
        try:
            valor ==val
        except ValueError:
            print("Debes escribir un número.")
            continue
        if valor < 0:
            print("Numero Invalido")
            continue
        else:
            break
        
        
def check(val): 
      
    
    if val > 0: 
        print("Positive") 
          
    
    elif val < 0: 
        print("Negative") 
          
    
    else: 
        print("Equal to zero") 
          
check(validacion(valor=validacion())) 

class CuentaCorriente(object):
    def __init__(self):
        self.valor=val
               
class CuentaDeAhorro(object):
    def __init__(self):
        self.valor2=val2

res=input("Desea ingresar un valor en la CUENTA CORRIENTE s/n: ")  
while True:
    res=input("Desea ingresar un valor s/n: ")  
    if res=="s" or res=="S":
        val = int(input("Ingrese un nuevo valor: "))
        
        salval=salval+val
    else:
        print("El saldo actual de esta cuenta es de:",salval )
        break
        
    
res=input("Desea ingresar un valor en la CUENTA DE AHORROS s/n: ")     
while True:
    res=input("Desea ingresar un valor s/n: ")        
    if res=="s" or res=="S":
        val2 = int(input("Ingrese el valor de la cuenta de ahorros: "))
        validar=validacion(val2)
        
        salval2=salval2+val2
    else:
        print("El saldo actual de esta cuenta es de:",salval2 )
        break 
    

print("Cuenta Corriente: ", salval)
print("Cuenta DE Ahorros: ", salval2)
print("TOTAL DE EFECTIVO: ", salval+salval2)


while True:
    res=input("Desea ingresar un retiro s/n: ")  
    if res=="s" or res=="S":
        val3 = int(input("Ingrese un nuevo retiro: "))
        validar=validacion(val3)
        retiro=retiro+val3
        st=salval-retiro
        TT=salval+salval2
        retiro3=retiro+retiro2
        TTT=TT-retiro
        
        if st<=0:
            print("El retiro a sobrepasado el saldo de la cuenta corriente se retirara de la cuenta asociada")  
            res3=input("Desea realizar un nuevo retiro s/n: ")
            if res3=="s" or res3=="S":
                while True:
                    res3=input("Desea realizar un nuevo retiro s/n: ")
                    if res3=="s" or res3=="S":
                        val3 = int(input("Ingrese un nuevo retiro: "))
                        validar=validacion(val3)
                        retiro2=retiro2+val3
                        
                        st2=TT-retiro-retiro2
                        print("Saldo actual: ", st2)
                    else:
                        print("FIN DEL PROGRAMA")
                        break
            else:
                print("FIN DEL PROGRAMA")
                break
                
        if TTT<0:
            print("NO SE PUEDE REALIZAR ESTA ACCION FIN DEL PROGRAMA")
            break
        
    else:
        print("FIN DEL PROGRAMA")
        break
    
