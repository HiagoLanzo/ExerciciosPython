# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato
soma = prod1 = menor = cont = 0
barato = ''
print('='*30)
print('     LOJA SUPER BARATÃO')
print('='*30)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        prod1 += 1
    soma += preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {prod1} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

