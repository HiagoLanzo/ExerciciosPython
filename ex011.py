#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
a = float(input('Digite a altura da sua parede: '))
l = float(input('Digite a largura da sua parede: '))
rq = a*l
lt = rq/2
print('Sua parede tem {} x {} e sua area é de {:.3f}m²'.format(a,l,rq))
print('Para poder pintar essa parede, voce precisara de {:.2f}L de tinta.'.format(lt))
