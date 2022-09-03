#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto; em até 2x no cartão: preço formal; 3x ou mais no cartão: 20% de juros
preco = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO 
[ 1 ] a vista no dinheiro 
[ 2 ] a vista no cartão 
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    pag = preco - (preco*10/100)
elif opcao == 2:
    pag = preco - (preco*5/100)
elif opcao == 3:
    pag = preco
    parc = preco / 2
    print('Sua compra sera parcelada em 2X de R${:.2f}'.format(parc))
elif opcao == 4:
    pag = preco + (preco*20/100)
    totpa = int(input('Quantas parcelas? '))
    parc = pag / totpa
    print('Sua compra parcelada em {:.2f}X  de R${:.2f} com juros'.format(totpa,parc))
print('Sua compra de R${:.2f}, vai custar R${:.2f}'.format(preco, pag))