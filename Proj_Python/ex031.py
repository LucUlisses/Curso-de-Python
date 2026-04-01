distancia = float(input('Qual a distancia da sua viagem? '))
valor1 = distancia * 0.50
valor2 = distancia * 0.45
if valor1 <= 200:
    print('Sua viagem custará R${:.2f}'.format(valor1))
else:
    print('Sua viagem custará {:.2f}'.format(valor2))