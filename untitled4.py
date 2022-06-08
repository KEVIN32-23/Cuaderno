# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:01:50 2022

@author: lab
"""

SUMA=0
list=[]
for i in range(1, 11):
    valor=int(input("ingrese un valor entero : "))
    list.append(valor)
    SUMA+=valor
print("el valor de la suma es: ",SUMA)
print("el promedio es: ",SUMA/10)
print("la list es",list) 