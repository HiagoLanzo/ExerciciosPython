# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
from math import factorial
n = int(input('Digite um numero para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))