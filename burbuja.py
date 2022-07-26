# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 22:40:25 2022

@author: User
"""

import time #libreria de tiempo para usar sleep(1)
import random #libreria random usar randinit(50,100)

ingreso = input("Ingrese el tamaño del vector:") #Leemos el valor ingresado
dimension = int(ingreso) #Convertimos el valor a un entero
vector = [] #Declaramos un vector vacio
 #Lazo for que nos permite llenar el vector con numeros aleatorios
for i in range(dimension):
    vector.append(random.randint(50, 100)) #Numero aleatorio entre 50 y 100
    print(f"El valor en la posición {i+1} es {vector[i]}") #Imprimimos el valor
    time.sleep(1) #Esperamos un segundo
#Método burbuja
for i in range(dimension):
    for j in range(dimension - 1):
        if(vector[j] > vector[j + 1]):
            aux = vector[j]
            vector[j] = vector[j + 1]
            vector[j + 1] = aux
#Imprimimos el vector ordenado
print("\nVector ordenado")
for i in range(dimension):
    print(f"El valor en la posición {i+1} es {vector[i]}")
    time.sleep(1)
    
    
