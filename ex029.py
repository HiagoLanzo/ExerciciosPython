# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = int(input('Qual velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! A velocidade permitida é 80Km/h')
    multa = (vel - 80) * 7
    print('O valor da multa é de {}'.format(multa))
print('Tenha um bom dia! Dirija com cuidado!')