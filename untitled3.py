# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 08:40:13 2022

@author: Alumno
"""

filas = int(input("Ingrese el numero de filas"))
columnas = int(input("Ingrese el numero de columnas"))

range (4, 30)
while filas > 4:
     print(filas)
     if filas == 30 :
         break
     filas -=30
     
matriz = []
for i in range (filas):
    matriz.append([])
    for j in range (columnas):
        valor = float(input ("Fila {}, columna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)
        
print 
     
    
