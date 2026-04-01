num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXAGONAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para HEXAGONAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção INVÁLIDA! Tente novamente')