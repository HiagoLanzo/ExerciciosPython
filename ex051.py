# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('      10 TERMOS DE UMA PA')
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = pt + (10-1)*r
for c in range(pt,d+r,r):
    print('{}'.format(c), end='-> ')
print('Acabou')