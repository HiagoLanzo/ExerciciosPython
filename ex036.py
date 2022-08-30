casa = float(input('Valor casa: R$ '))
sal = float(input('Salario do comprador: R$ '))
anos = int(input('Em quantos anos de finaciamento? '))
pres = casa / (anos*12)
print('Para pegar uma casa de R${} em {} anos, a prestação sera de {:.2f}'.format(casa,anos,pres))
if pres > (30/100*sal):
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo CONCEDIDO!')