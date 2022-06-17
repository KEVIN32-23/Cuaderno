# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 08:01:24 2022

@author: User
"""

def fiib(n) :
    a = 0
    b = 1
    
    
    for k in range(n):
        c = a+b
        a = b
        b = c
        
        
    return b

for x in range(8) :
    print (fiib(x))
    