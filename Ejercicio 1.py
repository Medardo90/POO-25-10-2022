print("----------Vehiculo----------")
class Vehiculo(object): 
    def __init__(self, var, marc, mol):
        self.marca= marc
        self.modelo=mol
        self.color=var 
    def acel(self,estado):
        print("Estado del Vehiculo:", estado)
        
obj_vehiculo1= Vehiculo("amarrillo","Chevrolet","Onix")
print("Color:",obj_vehiculo1.color)
print("Marca:",obj_vehiculo1.marca)
print("Modelo:",obj_vehiculo1.modelo)
obj_vehiculo1.acel("Estacionado")     
print("")
obj_vehiculo2= Vehiculo("Azul","Chevrolet","D-MAX HI RIDE")
print("Color:",obj_vehiculo2.color)
print("Marca:",obj_vehiculo2.marca)
print("Modelo:",obj_vehiculo2.modelo)
obj_vehiculo2.acel("En movimiento")     
print("")
obj_vehiculo3= Vehiculo("Blanco","Chevrolet","Tracker Turbo")
print("Color:",obj_vehiculo3.color)
print("Marca:",obj_vehiculo3.marca)
print("Modelo:",obj_vehiculo3.modelo)
obj_vehiculo3.acel("Detenido")     
print("")

print("----------Vehiculo Hibrido----------")
class hibrido (Vehiculo):
    pass
fortuner= hibrido("negro","Chevrolet","Fortuner")
print ("color:", fortuner.color)
print ("Marca:",fortuner.marca)
print ("Modelo:",fortuner.modelo)
fortuner.acel("Incautado")   

print("----------Taxonomia----------")
class taxonomia: #creacion de clase
    def __init__(self, cl, fam, odn, nm):
        self.familia= fam
        self.orden=odn
        self.clase=cl
        self.name=nm
    def healt(self,estado):
        print("Estado del animal:", estado)
        
obj_animal= taxonomia("Canidae","Mammalia","Carnivoro","Lobo")
print("Nombre:",obj_animal.name)
print("Familia:",obj_animal.familia)
print("Orden:",obj_animal.orden)
print("Clase:",obj_animal.clase)
obj_animal.healt("Enfermo")
print("")
obj_animal2= taxonomia("Mammalia","Felidae","Carnivoro","Leon")
print("Nombre:",obj_animal2.name)
print("Familia:",obj_animal2.familia)
print("Orden:",obj_animal2.orden)
print("Clase:",obj_animal2.clase)
obj_animal2.healt("Saludable")
print("")
obj_animal3= taxonomia("Mammalia","Ursidae","Carnivoro","Oso Polar")
print("Nombre:",obj_animal3.name)
print("Familia:",obj_animal3.familia)
print("Orden:",obj_animal3.orden)
print("Clase:",obj_animal3.clase)
obj_animal3.healt("Recien Nacido")
print("")



print("----------Lego----------")
class Lego: 
    def __init__(self, marc, mol, dim):
        self.marca= marc
        self.modelproduccion =mol
        self.dimensiones=dim
    def CC(self,estado):
        print("Control de calidad:", estado)
        
obj_Lego= Lego("Play Doh","SDQWR","2x3x1.6")
print("Marca:",obj_Lego.marca)
print("Modelo de Produccion:",obj_Lego.modelproduccion)
print("Dimension:",obj_Lego.dimensiones)
obj_Lego.CC("Regular")
print("")
obj_Lego2= Lego("Duplox","TUXPR","5x5x2")
print("Marca:",obj_Lego2.marca)
print("Modelo de Produccion:",obj_Lego2.modelproduccion)
print("Dimension:",obj_Lego2.dimensiones)
obj_Lego2.CC("Defectuoso")
print("")
obj_Lego3= Lego("LEGO","MSFTR","4x6x1")
print("Marca:",obj_Lego3.marca)
print("Modelo de Produccion:",obj_Lego3.modelproduccion)
print("Dimension:",obj_Lego3.dimensiones)
obj_Lego3.CC("Defectuoso")
print("")
print("----------Lego Star Wars----------")
class Lego_Star_Wars (Lego):
    pass
Luke_Skywalker= Lego_Star_Wars("LEGO","Lego.lukeSkywalker0569","2.5x4")
print ("color:", Luke_Skywalker.marca)
print ("Marca:",Luke_Skywalker.modelproduccion)
print ("Modelo:",Luke_Skywalker.dimensiones)