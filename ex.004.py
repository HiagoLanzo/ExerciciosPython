# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
#aqui iremos trabalhar com métodos de teste de tipo
a = input('Escreva algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Está em maisculas? ', a.isupper())
print('Está em minusculasw ', a.islower())
print('Está capitalizada? ', a.istitle())

