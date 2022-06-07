# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 08:36:56 2022

@author: Alumno
"""

def direction(calle,barrio,ciudad):
    print("su direccion es:")
    print("su ciudad es: ",ciudad)
    print("El barrio de entrega es: ",barrio)
    print("La calle de su domicilio es: Av: ",calle)
    
ci=input("Ingrese la ciudad")
cl=input("Ingrese la calle de entrega")
ba=input("Ingrese el sector de referencia para el entrega")

direction(cl, ba, ci) 
direction("SO-34, Nueva Aurora, Quito") 