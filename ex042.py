t1 = float(input('Primeiro Segmento: '))
t2 = float(input('Segundo Segmento: '))
t3 = float(input('Terceiro Segmento: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os segmentos PODEM formar um triângulo ', end='')
    if t1 == t2 == t3:
        print('EQUILÁTERO!')
    elif t1 != t2 != t3 != t1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos NÃO PODEM formar um triângulo')
