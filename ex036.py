casa = float(input('Qual valor da casa?R$ '))
salário = float(input('Qual seu salário?R$ '))
anos = int(input('Quantos anos de prestação? '))
prestação = casa / (anos * 12)
mínimo = salário * 30/100
print('Para pagar uam casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(" a prestação será de R${:.2f}".format(prestação))
if prestação <= mínimo:
    print('Seu Empréstimo foi NEGADO')
else:
    print('Seu empréstimo foi AUTORIZADO')