velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado em R${:.2f} por exceder o limite de velocidade de 80Km/h'.format(multa))
else:
    print('Dirija com segurança e tenha umm bom dia!')