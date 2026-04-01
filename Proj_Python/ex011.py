larg = float(input("Informe a largura: "))
alt = float(input("Informe a altura: "))
area = larg * alt
print("A parede tem dimensão de {} x {} e sua area equivale a {:.2f}".format(larg, alt, area))
tinta = area / 2
print("Para pintar a parede que possui uma area de {:.2f}, serao necessarios {:.2f}L de tinta".format(area, tinta))

