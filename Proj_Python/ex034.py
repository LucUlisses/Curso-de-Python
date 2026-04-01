salario = float(input('Digite seu salário: R$'))
a1 = salario + (salario * 10/100)
a2 = salario + (salario * 15/100)
if salario <= 1250.00:
    print('Seu novo salário será R${:.2f}'.format(a2))
else:
    print('Seu novo salário será R${:.2f}'.format(a1))
