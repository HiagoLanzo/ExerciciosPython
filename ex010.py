#: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
n=float(input('Quanto dinheiro vc tem na carteira? R$'))
d = n/3.27
print('Com R${:.2f} voce pode comprar U${:.2f}'.format(n,d))