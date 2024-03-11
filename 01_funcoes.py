def imc (peso,altura):
    resultado = peso / altura ** 2
    return resultado

print (f"O imc de uma pessoa com 78 kg e 1,83 é {imc(78, 1.83)} ")

###########################################################################

from math import pi

def calc_area(base,altura, tipo):
    if tipo == 'R':    #retangulo
        return base * altura
    elif tipo == 'T':  #triangulo
        return base * altura / 2
    elif tipo == 'E': #elipse
        return (base / 2) * (altura / 2) * pi   
    else: 
        return None

print (f"área do retangulo 22 x 47: {calc_area(22, 47, 'R')}")
print (f"Área do triangulo 12,5 x 25:{calc_area(12.5, 25, 'T')} ")
print (f"Área elipse 20x30: {calc_area(20, 30, 'E')}")
print (f"área invalida 8x11,5:{calc_area(8,11.5,'W')}")
