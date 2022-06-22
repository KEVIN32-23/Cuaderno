# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:44:05 2022

@author: User
"""

from math import sqrt,sin,cos,tan,pi,factorial
def potencia(a,b):
  res = pow(a,b)
  return res
def ecuacionCuadratica(a,b,c):
  discriminante = b*b-4*a*c
  if discriminante < 0:
    print('La ecuación no tiene soluciones reales.')
  else:
    raiz = sqrt(discriminante)
    x_1 = (-b + raiz)/(2*a)
    if discriminante != 0:
      x_2 = (-b - raiz)/(2*a)
      print('Las soluciones son: ', 'X1 = ',x_1,'\nX2 = ',x_2)
    else:
      print('La unica solucion es: X = ',x_1)
def serieInfinita(x,In):
  suma=x  
  for i in range(0,In):  
    valor=pow(x,i)/factorial(i) 
    suma += valor  
    print('Iteración: ',i,'\nValor: ',valor,'\nSuma: ',suma)
print('---------------------Potencia--------------------------------')
while True:
  base = int(input('Ingrese la base: '))
  exponente = int(input('Ingrese el exponente: '))
  if base >= 0 and exponente >= 0:
    break
p = potencia(base,exponente)
print('La potencia es igual a: ', p,'\n')
print('------------------Ecuación cuadratica-------------------------------')
a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))
c = float(input('Ingrese el valor de c: '))
ecuacionCuadratica(a,b,c)
print('\n--------------------Sucesión del os números---------------------------')
n = int(input('Ingrese el numero n: '))
i = 0
res = 0
while i < n:
  l = pow(2,n)
  res += l
  n -= 1
print('Resultado: ',res)
print('\n--------------------Funciones trigonometricas seno, coseno, tangente-------------------------')
ang1 = (30* pi)/180
ang2 = (60* pi)/180
ang3 = (90* pi)/180
ang4 = (120* pi)/180
sin1 = sin(ang1)
cos1 = cos(ang1)
tan1 = tan(ang1)
sin2 = sin(ang2)
cos2 = cos(ang2)
tan2 = tan(ang2)
sin3 = sin(ang3)
cos3 = cos(ang3)
tan3 = tan(ang3)
sin4 = sin(ang4)
cos4 = cos(ang4)
tan4 = tan(ang4)
print('Sin: 30 = ',sin1)
print('Cos: 30 = ',cos1)
print('Tan: 30 = ',tan1)
print('Sin: 60 = ',sin2)
print('Cos: 60 = ',cos2)
print('Tan: 60 = ',tan2)
print('Sin: 90 = ',sin3)
print('Cos: 90 = ',cos3)
print('Tan: 90 = ',tan3)
print('Sin: 120 = ',sin4)
print('Cos: 120 = ',cos4)
print('Tan: 120 = ',tan4)
print('---------------------------Serie infinita-------------------------')
x = int(input('Escriba el valor de x: '))
while True:
  In = int(input('Escriba el numero n iterable: '))
  if In > 0:
    break
serieInfinita(x,In)

