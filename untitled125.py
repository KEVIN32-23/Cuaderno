# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 00:47:11 2022

@author: User
"""

dict1={"nombre":"Kevin",
       "cedula":"1753972619",
       "edad":"20",
       "correo":"kevin08-00pilco@hotmail.com",}

caracteres = len("nombre")
tipo = dict1
if tipo == True:
    if caracteres < 1:
        print("Se debe ingresar al menos 1 caracter")
    elif caracteres > 25:
        print("Debe contener menos de 25 caracteres")
    else:
        print("nombre", "cedula", "edad", "correo")
    
print(dict1)
print(dict1["nombre"])
print(dict1["cedula"])
print(dict1["edad"])
print(dict1["correo"])




