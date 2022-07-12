# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 01:06:31 2022

@author: User
"""

def ordena(lista):
    long=len(lista)-1
    
    for i in range (0, long):
        
        for j in range (0, long):
            
            if lista[j]> lista[j+1]:
                
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                
    return lista
lista=[50,30,200,52,34,1001,5]
print("Antes de ordenas: ")
print(lista)
print("Despues de ordenar: ")
print(ordena(lista))
