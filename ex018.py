# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
an = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(an)) # tem q converter de graus para radianos!
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O angulo de {} tem o seno de {:.2f}'.format(an,seno))
print('O angulo de {} tem o cosseno de {:.2f}'.format(an,cos))
print('O angulo de {} tem a tangente de {:.2f}'.format(an,tan))

