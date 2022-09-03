# Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
itens = ('Pedra','Papel', 'Tesoura')
computador = randint(0,2)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
if computador == 0: #jogou pedra
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('Jogador GANHOU')
    elif jogador == 2:
        print('Computador GANHOU')
    else:
        print('Jogada invalida')
elif computador == 1:#jogou papel
    if jogador == 0:
        print('Computador GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador GANHOU')
    else:
        print('Jogada invalida')
elif computador == 2: #jogou tesoura
    if jogador == 0:
        print('Jogador GANHOU')
    elif jogador == 1:
        print('Computador GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')
