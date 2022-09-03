# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso;  Entre 18,5 e 25: Peso Ideal
# IMC entre 25,0 e 29,9 Kg/m2: sobrepeso;
# IMC entre 30,0 e 34,9 Kg/m2: obesidade grau I;
# IMC entre 35,0 e 39,9 Kg/m2: obesidade grau II;
# IMC maior do que 40,0 Kg/m2: obesidade grau III
peso = float(input('Qual seu peso: (KG) '))
altura = float(input('Qual sua altura: (M) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5 :
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Obesidade Grau I')
elif imc <= 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III')