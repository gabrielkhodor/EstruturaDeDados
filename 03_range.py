# range é uma função que gera uma faixa de números
# é muito usado em associação de listas

# 1)range() com *um* parametro
# gera uma faixa numerica que vai de (0) zero até o valor
# do parametro - 1

for num in range(10):
    print(num)

print("-" * 60)

# 2) range() com *dois* parametros
# 1° parametro -> valor inicial
# 2° parametro -> valor final da faixa (não incluido)

for x in range(10,16):
    print(x)

print("-" * 60)# separador

# 3) range com *tres* parametros
# 1° parametro -> valor inicial
# 2° parametro -> valor final da faixa (não incluido)
# 3° parametro -> passo (intervalo entre um número e outro)

for n in range(1,22,3):
    print(n)

print("-" * 60)# separador

# range() com passo negativo

for i in range(10,0,-1): #contagem regressiva de 10 a 1
    print(i)

