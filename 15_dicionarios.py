"""
DICIONÁRIO é uma estrutura de dados nativa da linguagem python
capaz de aramzenar multiplos valores em uma única variável, por meio de pares de 
chaves-valor (key value)
um dicionário é delimitado por chaves{}, diferentemente da lista, que tem posições numeradas,
o dicionário possui posições nomeadas de um dicionário(ou seja um par de chave-valor) é chamado de PRORPIEDADE


"""
pessoa = {
    #chave-valor
    "nome": "Orozimbo Oliveira Ozorio",
    "sexo": "M",
    "idade": 72,
    "peso": 76,
    "altura": 1.66,
    "aposentado": True,
    "filhos" : ["Zeferino","Adamastor", "Gercina"]
}

#############
# Acessando ao valor das propriedades

print("Nome: ")

for i in pessoa:
    print(i)
#print(pessoa)