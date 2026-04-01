from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM!')
elif idade >= 10 and idade <= 14:
    print('Categoria: INFANTIL!')
elif idade >=15 and idade <= 19:
    print('Categoria: JÚNIOR!')
elif idade >= 20 and idade <=25:
    print('Categoria: SÊNIOR!')
elif idade > 25:
    print('Categoria: MASTER!')
