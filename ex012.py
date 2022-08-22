#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Qual preço do produto? R$'))
d = p - (p*5/100)
print('O produto custava R${} , na promoção de 5% de desconto vai custar R${:.2f}'.format(p,d))