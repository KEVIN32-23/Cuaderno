# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 07:54:21 2022

@author: Alumno
"""

def suma(*a):
    print("\nTipo de datos del argumento",type(a))
    sum=0
    for n in a:
        sum +=n
        #sum=suma+n
        
    print("Suma:",sum)
    
suma(3)
suma(1)
suma(3,5)
suma(4, 5, 6, 7)

