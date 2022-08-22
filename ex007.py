#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n0 = input('Digite o nome da(o) aluna(o): ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
#m = (n1+n2)/2
#print('A media do aluno é {:.2f}'.format(m))
print('Nota 1 = {} e nota 2 = {}. \nA média da(o) aluna(o) {} é {:.1f}.'.format(n1, n2, n0, (n1+n2)/2))
