# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for sete in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(sete)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('{} pessoas são maiores de idade e {} pessoas são menores de idade.'.format(maior, menor))