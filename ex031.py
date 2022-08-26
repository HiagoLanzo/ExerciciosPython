#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = int(input('Qual distancia da sua viagem? '))
print('Voce fazer uma viagem de {}km'.format(dist))
if dist <= 200:
    print('O valor da passagem é R${:.2f}.'.format(dist * 0.5))
else:
    print('O valor da passagem é R${:.2f}.'.format(dist * 0.45))