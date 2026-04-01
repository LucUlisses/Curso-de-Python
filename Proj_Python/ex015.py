dias = int(input("Quantos dia(s) alugado(s)? "))
km = float(input("Quantos Km rodado? "))
valor = ( dias * 60) + ( km * 0.15)
print("O valor a ser pago no total sera de R${:.2f}".format(valor))
