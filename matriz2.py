# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:51:29 2022

@author: User
"""

filas = int(input("Ingrese el numero de filas"))
columnas = int(input("Ingrese el numero de columnas"))

if filas<30 or filas>4:
    
    matriz = []
for i in range (filas):
    matriz.append([0] * columnas)
    for j in range (columnas):
        valor = float(input("fila {}, columna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)
        
print ()
for fila in matriz:
    print("[", end=" ")
    for elemento in fila:
            print("{:30.4f}".format(elemento), end=" ")
    print("]")
print ()

    