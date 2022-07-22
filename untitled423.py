# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 23:47:51 2022

@author: User
"""

filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))

matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input("Fila {}, columna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)
        
print()
for fila in matriz:
    print("[", end="")
    for elemento in fila:
        print("{:8}".format(elemento), end="")
    print("]")
    
print()