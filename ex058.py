# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.
from random import randint
pc = randint(0,10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi? ')
acertou = False
t = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    t += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez.')
        elif jogador > pc:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabens!'.format(t))
