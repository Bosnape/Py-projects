from math import sqrt
cateto1 = float(input("c1: "))
cateto2 = float(input("c2: "))
h = float(input("h: "))

if h == 0:
    h = sqrt(cateto1 ** 2 + cateto2 ** 2)
    print("hipotenusa = {}".format(h))
elif cateto1 == 0:
    cateto1 = sqrt(h ** 2 - cateto2 ** 2)
    print("cateto 1 = {}".format(cateto1))
else:
    cateto2 = sqrt(h ** 2 - cateto1 ** 2)
    print("cateto 2 = {}".format(cateto2))



