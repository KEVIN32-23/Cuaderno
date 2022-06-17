# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:48:15 2022

@author: User
"""

a = 21
def es_primo(num) :
    contador=0
    for i in range(1, num+1) :
        if num / i == 0:
            contador += 1
            print(i)
            
    if contador == 2:
        return True
    else: 
        return False
print(es_primo(2))










    