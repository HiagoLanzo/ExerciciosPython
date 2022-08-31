# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#  se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou
#  se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade == 18:
    print('Voce tem que se alistar esse ano')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o seu alistamento'.format(saldo))
else:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado há {} anos'.format(saldo))
