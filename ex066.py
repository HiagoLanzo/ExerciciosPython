#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
soma = quant = num = 0
while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        break
    quant += 1
    soma += num
print(f'Voce digitou {quant} numeros e a soma entre eles foi de {soma}')
