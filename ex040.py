# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:.
# Média abaixo de 5.0: REPROVADO – Média entre 5.0 e 6.9: RECUPERAÇÃO – Média 7.0 ou superior: APROVADO
nota = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota+nota2)/2
print('Tirando {} e {}, a media do aluno é {:.2f}'.format(nota,nota2,media))
if media < 5:
    print('O aluno esta reprovado')
elif 7 > media >= 5:
# elif media >= 5 and media < 7:
    print('O aluno está de recuperação')
else:
    print('O aluno foi aprovado')