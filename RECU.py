# -*- coding: utf-8 -*-
"""
Created on Fri May 27 01:51:47 2022

@author: User
"""

hora=int(input("Ingrese una hora hh "))
minutos=int(input("Ingrese un valor en minutos mm "))
segundos=int(input("Ingrese un valor en segundos ss "))
error=False

if hora >23 or hora <0:
    print ("El dato de la hora no es correcto")
    error=True
    
if minutos <0 or minutos >59 :
    print (" El dato de los minutos no es correcto")
    error=True
if segundos<0 or segundos >59:
    print("El dato de los segundos no es correcto: ")
    error=True
if error==False :
    print("Puedo continuar: ")
    sextra=int(input("ingrese el valor de los segundos extras"))
    if sextra<0:
        print("El valor de los segundos extras es invalido")
    else:
        print("puedo continuar")
        ensegundos=(hora*3600)+(minutos*60)+segundos
        suma=sextra+ensegundos
        hh=int(suma/3600)
        mm=int((suma/60)-(hh*60))
        ss=int((suma-(mm*60)-(hh*3600)))
        print(hh,mm,ss)
if error==True :
   print("Puedo continuar")
   sextra=int(input("ingrese el valor de los segundos extras"))
   if sextra>0:
       print("El valor de los segundos extras es valido")
   else: 
       print("Puedo continuar")
       ensegundos=(hora*7200)+(minutos*120)+segundos
       suma=sextra+ensegundos
       hh=int(suma/7200)
       mm=int((suma/120)+(hh*120))
       ss=int((suma+(mm*120)+(hh*7200)))
       print(hh,mm,ss)
print("Fin del programa")