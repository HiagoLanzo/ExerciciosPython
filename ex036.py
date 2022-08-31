# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor casa: R$ '))
sal = float(input('Salario do comprador: R$ '))
anos = int(input('Em quantos anos de finaciamento? '))
pres = casa / (anos*12)
print('Para pegar uma casa de R${} em {} anos, a prestação sera de {:.2f}'.format(casa,anos,pres))
if pres > (30/100*sal):
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo CONCEDIDO!')