# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:30:32 2022

@author: Kevin Pilco
"""

partida1=int(input("Ingrese la 1ra partida: "))
partida2=int(input("Ingrese la 2da partida: "))
partida3=int(input("Ingrese la 3ra partida: "))
if partida1>=partida2 and partida3 >=partida2:
    resultado=partida1+partida3
elif partida1>=partida3 and partida2 >=partida3:
    resultado=partida1+partida2
else:
    resultado=partida2+partida3
    
print("el resultado de la calificacion es:",resultado)
    