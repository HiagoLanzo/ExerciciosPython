# DESAFIO 35 Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2+ r3 and r2 < r1 +r3 and r3 < r1+ r2:
    print('Os segmentos acima podem formar um triangulo1')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISOSCELES')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
else:
    print('Os segementos acima não podem formar um triangulo')