salario = float(input("Informe o salario do funcionari: R$"))
novo = salario + (salario * 15 / 100)
print("O funcionario que ganhava R${:.2f}, agora com o aumento ira ganhar R${:2f}".format(salario, novo))
