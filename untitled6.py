# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:50:20 2022

@author: lab
"""

contador1=0
contador2=0
promedio=0
suma=0
lista=[]
for i in range(1,6):
    valor=float(input("ingrese la estatura:"))
    suma+=valor
    lista.append(valor)
promedio=suma/5
print("El promedio total es:",promedio)
for j in lista:
    if lista[j]>promedio: 
        contador1+=1
    else:
        contador2+=1
print("Hay",contador1,"mayor que el promedio")
print("Hay",contador2,"menor que el promedio")