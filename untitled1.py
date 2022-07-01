# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 08:20:42 2022

@author: Alumno
"""

filas = int(input("Ingrese el numero de filas"))
columnas = int(input("Ingrese el numero de columnas"))
 
matriz = []
for i in range (filas):
    matriz.append([])
    for j in range (columnas):
        valor = float(input ("Fila {}, columna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)
        
print 
