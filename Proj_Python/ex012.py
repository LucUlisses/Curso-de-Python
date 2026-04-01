valor = float(input("Digite o valor do produto: R$"))
novo = valor - (valor * 15 / 100)
print("O produto que era R${:.2f}, agora com o desconto equivale a R${:.2f}".format(valor, novo))
