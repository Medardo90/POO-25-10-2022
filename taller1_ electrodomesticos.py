import random
class Electrodomestico:
    def __init__(self):
        self.color="blanco"
        self.consumo="A"
        self.prebase="10 €"
        self.consumo=None
    def tabla(self):
        self.consumo= "A"
        self.consumo2= "B"
        self.consumo3= "C"
          
def precio_if():
    if refrigeradora.consumo=="A":
        print(" Precio: 100")
    elif refrigeradora.consumo=="B":
        print(" Precio: 80")
    elif refrigeradora.consumo=="C":
        print(" Precio: 60")

class lavadora():
    def __init__(self):
        self.color="blanco"
        self.consumo="A"
        self.prebase="10 €"
        self.consumo=None
        
    def tabla2(self):
        self.consumo= "Entre 0 y 19 kg"
        self.consumo2= "Entre 20 y 49 kg"
        self.consumo3= "Entre 50 y 79 kg"
        self.consumo4= "Mayor que 80 kg"

def precio_lavadora():
    if lavadora.consumo=="Entre 0 y 19 kg":
        print(" Precio: 10%") 
    elif lavadora.consumo=="Entre 20 y 49 kg":
        print(" Precio: 20%")
    elif lavadora.consumo=="Entre 50 y 79 kg":
        print(" Precio: 30%")
    elif lavadora.consumo=="Mayor que 80 kg":
        print(" Precio: 40%")
        
obj_c= Electrodomestico()
obj_l= lavadora()
obj_c.tabla()
obj_l.tabla2()

print(" ")
print(" ------------Valores Predeterminados de la tienda------------")
peso=int(input(" Ingrese el peso del objeto: "))
refrigeradora=Electrodomestico()

print(" Precio Base:",refrigeradora.prebase,"\n","Color:",refrigeradora.color,"\n",
      "Consumo energetico:",obj_c.consumo,"\n","Peso:",peso)

lista=["azul","rojo"]
refrigeradora.color=random.choice(lista)
listaconsumo=[obj_c.consumo,obj_c.consumo2,obj_c.consumo3]
refrigeradora.consumo=random.choice(listaconsumo)
print(" ")
print(" //////////////////////////////////////////////////////")
print(" ")
for i in range(1):
    print(" ------------Refrigeradora------------")
    print(" Color refrigeradora: ",refrigeradora.color,"\n","Consumo energetico:",refrigeradora.consumo,
          "\n","Peso:",peso,"\n",precio_if())  

lavadora.color=random.choice(lista)
listaconsumo=[obj_l.consumo,obj_l.consumo2,obj_l.consumo3,obj_l.consumo4]
lavadora.consumo=random.choice(listaconsumo)
print(" ")
for i in range(1):
    print(" ------------Lavadora------------")
    print(" Color lavadora: ",lavadora.color,"\n","Carga:",lavadora.consumo,
          "\n","Peso:",peso,"\n",precio_lavadora())  

    


   


