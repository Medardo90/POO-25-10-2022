# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:37:40 2022

@author: Patricio Haro
"""

class Sensor:
    def __init__(self, tag, size):
        self.tag=tag   
        self.state= False
        self.size= size
        
    def activar(self,activate):
        self.state = activate 
        print("sensor state:", self.state)
        
class Sensorlight(Sensor):
    def __init__(self, tag, size,type):
        self.type= type
        Sensor.__init__(self, tag, size)
        
class SensorManager:
    def __init__(self,sensorligh):
        self.sensorligh= sensorligh
        self.sensorTemperature= None
        
    def activatesensor(self,activate):
        self.selsorLight.activar(activate)
        
class Vehiculo:
    def __init__(self):
        self.sensorLight=SensorLight(1,"off","pothotransitor")
        self.SensorManager= SensorManager(self,sensorLight)
        
    def mando(self,orden):
        self.sensorManager=activateSensor(orden) 
        
obj_vehiculo = Vehiculo()
obj_vehiculo =mando(True)
        
        
       
    
    
        
# ser= Sensor()
# print(ser.activar)

