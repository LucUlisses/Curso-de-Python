from math import radians, sin, cos, tan
an = float(input("Digite o valor do angulo: "))
sen = sin(radians(an))
print("O angulo informado tem o seno de {:.2f}".format(sen))
cos = cos(radians(an))
print("O angulo informado possui o cosseno de {:.2f}".format(cos))
tan = tan(radians(an))
print("O angulo informado possui a tangente de {:.2f}".format(tan))
