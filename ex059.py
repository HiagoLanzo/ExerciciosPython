#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao !=5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa''')
    opcao = int(input('Qual sua opção: '))
    if opcao == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif opcao == 2:
        print('{} X {} = {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('{} é o maior numero'.format(n1))
        else:
            print('{} é o numero maior'.format(n2))
    elif opcao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opção invalida. Tente novamente')
    print(sleep(1.5))
    print('===============================')
print('Fim do programa! Volte sempre! ')
