class Cuentadeahorros:
    def __init__(self,saldo_a):
        self.saldo_a=float(0)
        
        
class Cuentacorriente:
    def __init__(self,saldo_c):
        self.saldo_c=float(0)
       
class CI:
    def __init__(self,apellidos, nombres, nacionalidad, nacimiento, lnacer, ncedula):
        self.apellido='Naranjo Ponce'
        self.nombre='Darwin Sebastian'
        self.nacionalidad='Ecuatoriano'
        self.nacimiento='05/03/2003'
        self.lnacimiento='STO. DOMINGO STO.DOMINGO BOMBOLI'
        self.ncedula='2351001033'
class cuentaperson(Cuentadeahorros,Cuentacorriente,CI):
   pass

cuenta=cuentaperson('')
while True:
    print('Que desea realizar','\n','Retiro (1','\n','Ingreso (2','\n','Saldo (3')
    ris=int(input('Que desea hacer:'))
    if ris==1:  
        print('Desea retirar dinero de su:','\n','Cuenta de ahorros (1','\n','Cuenta corriente (2')
        r=int(input(':'))
        if r==1:
                dinero_a=float(input('Cuanto dinero desea retirar:'))
                cuenta.saldo_a=cuenta.saldo_a-dinero_a
                if cuenta.saldo_a<0:
                    cuenta.saldo_a=cuenta.saldo_a+dinero_a
                    print('No puede retirar dinero, saldo insuficiente.')
                else:
                    print('Su retiro a sido exitoso')
                    
        if r==2:
            while True:
                dinero_c=float(input('Cuanto dinero desea retirar:'))
                cuenta.saldo_c=cuenta.saldo_c-dinero_c
                if cuenta.saldo_c<0:
                    cuenta.saldo_c=cuenta.saldo_c+dinero_c
                    print('No puede retirar dinero, saldo insuficiente.','\n','Desea retirar dinero de su cuenta de ahorros vinculado.')
                    qc=int(input('Si/No :'))
                    if qc=='Si' or qc=='si' or qc=='SI':
                       cuenta.saldo_a=cuenta.saldo_a-dinero_a
                       if cuenta.saldo_a<0:
                           cuenta.saldo_a=cuenta.saldo_a+dinero_a
                           print('No puede retirar dinero, saldo insuficiente.')
                else:
                    print('Su retiro a sido exitoso')
                    break
    ##################################################################################################
    if ris==2:  
        print('Desea ingresar dinero en su:','\n','Cuenta de ahorros (1','\n','Cuenta corriente (2')
        r2=int(input(':'))
        if r2==1:
                dinero_a=float(input('Cuanto dinero desea ingresar:'))
                cuenta.saldo_a=cuenta.saldo_a+dinero_a
                print('Su dinero ha sido ingresado')
                
        if r2==2:
            dinero_c=float(input('Cuanto dinero desea ingresar:'))
            cuenta.saldo_c=cuenta.saldo_c+dinero_c
            print('Su dinero ha sido ingresado')
    #############################################################################################################################
    if ris==3:  
        print('Desea ver el saldo de su:','\n','Cuenta de ahorros (1','\n','Cuenta corriente (2')
        rs=int(input(':'))
        if rs==1:     
            print('El CI del titular es:','\n','Apellidos:',cuenta.apellido,
                  '\n','Nombres',cuenta.nombre,'\n','Nacionalidad:',cuenta.nacionalidad,
                  '\n','Fecha de nacimiento',cuenta.nacimiento,'\n','Lugar de nacimiento',cuenta.lnacimiento,
                  '\n','Número de cédula',cuenta.ncedula,'\n','El saldo de su cuenta de ahorros es :',cuenta.saldo_a,)
            
                
        if rs==2:
            print('El CI del titular es:','\n','Apellidos:',cuenta.apellido,'\n','Nombres',cuenta.nombre,'\n','Nacionalidad:',cuenta.nacionalidad,'\n','Fecha de nacimiento',cuenta.nacimiento,'\n','Lugar de nacimiento',cuenta.lnacimiento,'\n','Número de cédula',cuenta.ncedula,'\n','El saldo de su cuenta de ahorros es :',cuenta.saldo_c,)
        
    salir=input('Desea salir del banco, SI/NO :')
    if salir=='SI' or salir=='Si' or salir=='si':
        break