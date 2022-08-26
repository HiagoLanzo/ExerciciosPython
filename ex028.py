# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
from random import randint
num = randint(0, 5) #faz o computador pensar
print('Vou pensar em um numero entre 0 e 5. Tente advinhar..')
jog = int(input('Em que numero eu pensei? '))#jogador tenta advinhar
if num == jog:
    print('Voce acertou!')
else:
    print('Voce errou!')