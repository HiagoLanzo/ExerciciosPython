# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
v1 = int(input('Primeiro numero: '))
v2 = int(input('Segundo numero: '))
if v1 > v2:
    print('Primeiro numero é maior')
elif v2 > v1:
    print('Segundo numero maior')
else:
    print('Valores iguais')