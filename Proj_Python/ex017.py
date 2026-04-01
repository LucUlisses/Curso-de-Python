import math
co = float(input("Qual o cateto oposto? "))
ca = float(input("Qual o cateto adjacente? "))
hi = math.hypot(co,ca)
print("O valor da hipotenusa equivale a {:.2f}".format(hi))
