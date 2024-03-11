frutas = ["Laranja","maçã","uva","pera","mamão","abacate","amora"]

#para percorrer uma lista e exibir apenas seus elementos
#usamos a estrutura for..in já visto no arquivo n°2

for f in frutas:
    print(f)

print("-" * 60)#separador
#percorrendo uma lista em ordem inversa

for x  in reversed(frutas):
    print(x)

print("-" * 60)

# No entanto frequentemente precisamos exibir, alem do
#valor do elemento, também sua posição. nesse caso devevos
# usar a função for..in combinados com as funções range() e len()

for pos in range(len(frutas)):
    print(pos,":", frutas[pos])# acesso a posição

print("-" * 60)


# As vezes é necessário percorrer a lista de tráz para frente,
# mas tendo acesso a posição do elemento.Para isso
#  usamos a estrutura for..in ,len() e range() com três parâmetros

for i in range(len(frutas)-1,-1,-1):
    print(i, ":", frutas[i])

print("-" * 60)

