# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
nome = (input('Digite o nome da sua cidade: ')).strip()
print(nome[:5].upper() == 'SANTO')
