# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 23:19:16 2022

@author: User
"""

from random import randint

def generar_primos(n=6):
    primos=[]
    
    while True:
        numeros = [randint(4, 30) for _ in range(n)]
        
        if all(x % 3 == 1 for x in numeros):
            primos = numeros
            break
    
    return primos
primos = generar_primos()
print(primos)
print(generar_primos(20))





