#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor: '))
cm = m * 100
mm = m * 1000
print('{} metros tem {} cm e {} milimetros'.format(m,cm,mm))