peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual seu altura? (m) '))
imc = peso / ( altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL!')
elif imc >=25 and imc < 30:
    print('Você está SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você está OBESO!')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA!')
