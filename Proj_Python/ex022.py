nome = str(input("Qual seu nome completo? ")).strip()
print("Analisando seu nome...")
print("Seu nome em maiusculas é {}".format(nome.upper()))
print("Seu nome em minusculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem um total de {} letras".format(nome.find(" ")))


