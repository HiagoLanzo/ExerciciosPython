#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um numero: '))
d = n1 * 2
t = n1 * 3
rq = n1 ** (1 / 2)
print('O dobro do seu numero é {} e o triplo é {} e a raiz quadrada é {:.2f}\n'.format(d, t, rq))
#ou
print('O dobro de {} vale {}'.format(n1,(n1*2)))
print('O triplo de {} vale {} \nA raiz quadrada de {} vale {:.2f}'.format(n1 , (n1*3),n1, (n1**(1/2))))