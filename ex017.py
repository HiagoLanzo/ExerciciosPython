# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#from math import sqrt, pow
'''co = float(input('Comprimento cateto oposto: '))
ca = float(input('Comprimento cateto adjacente: '))
hi = (co ** 2 + ca ** 2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
#ou '''
from math import hypot
co = float(input('Comprimento cateto oposto: '))
ca = float(input('Comprimento cateto adjacento: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))