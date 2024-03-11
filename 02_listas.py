#LISTAS são uma estrutura de dados nativa da linguagem
#python.Elas permiem que varios 
#valores possam ser associados 

# lista de strings
legumes = ["batata", "cenoura", "beterraba", "mandioquinha", "batata doce"]

# lista de valores de varios tipos

mistureba = ["joaquim", 10, "ovo", 3]

nums = [2,4,6,7,9]

## operações sobre listas ##

#1) percursos

#percorrer uma lista significa visitar cada um de seus itens
#e fazer algo com ele. no exemplo abaixo, vamos printar cada um dos elementos

for leg in legumes:
    print(leg)

#traço separador
print("-" * 60)

# 2) inserção de um novo elemento no fim da lista
"""
for n in nums:
    print(n * 2)
"""

nums.append(6)
legumes.append('mandioca')

print(nums)
print(legumes)

# 3) inserção de um novo elemento em uma posição especifíca insert()
# Parametros
# 1° posição onde será feita a inserção
# 2° o novo elemento a ser inserido

# inserindo um novo elemento na quarta posição .

print('-' * 60)
legumes.insert(3, 'tomate')
print(legumes)

# inserindo um novo elemento na primeira posição
legumes.insert(0, 'milho')
print(legumes)
# separador
print('-' * 60)

# 4) Acessando valores, informados a respectiva posição.
print("Elemento na quinta posição",legumes[4])
print("Elemento da primeira posição",legumes[0])
print("Elemento da última posição",legumes[-1]) #contagem negativa pega o último elemento
print("Elemento na penultima posição,",legumes[-2])# pega o penultimo elemento


#traço separador
print('-' * 60)

# 5)Substituindo valores existentes

print("Antes:",legumes)

# substituindo o valor da quarta posição posição 3

legumes[3] = "vagem"

#substituindo o valor na posição 0 primeira posição

legumes[0] = "nabo"

#substituindo o valor na últoima posição posição -1

legumes[-1] = "inhame"

print("depois:",legumes)

print('-' * 60)

# 6)determinando a quantidade de elementos da lista len()
print("quantidade de elemntos da lista legumes:",len(legumes))
print("Quantidade de elementos da lista números",len(nums))

# traço separador
print('-' * 60)

# 7) Removendo o último elemento de uma lista: pop() (sem parametros)

print("Antes: ",legumes)
removido = legumes.pop() #remove a última posiçao sem nenhum parâmetro
print("Valor removido",removido)
print("Depois",legumes)

#traço separador
print('-' * 60)

# 8) Removendo um elemento por sua posição: pop() com parâmetro
removido = legumes.pop(3)   #remove o elemento na posição 3
print("Valor removido da posição 3 :",removido)
print(legumes)

removido = legumes.pop(0)
print("Valor remivido da primeira posição: ",removido)
print(legumes)

#traço separador
print('-' * 60)

# 9) Removendo um elemento por seu valor: remove()
removido = legumes.remove("mandioquinha") #não retorna valor, ele remove só não joga na variável
print("Valor removido", removido)
print(legumes)

#traço separador
print('-' * 60)

# 10) juntando (concatenando) duas listas: extend()

mais_legumes = ["abobrinha", "quiabo", "jiló", "cabotia", "cara"]

legumes.extend(mais_legumes)

print(legumes)

#traço separador
print('-' * 60)

# 11) Fatiando uma lista
# fatiar significa copiar um pedaço da lista (uma sub lista)
# para uma nova lista

# cria uma sublista que contem os elementos das posições 2 a 5
# (posição 6 não entra)

sublista2_5 = legumes[2:6]
print("Sublista de 2 a 5",sublista2_5)

# 12) Cria uma sublista que contém os elementos desde o inicio até
# a posição 6 (posição 7 não entra)

sublista_inicio_6 = legumes[:7]
print("Sublista do inicio até a posição 6",sublista_inicio_6)

# Cria uma sublista que contém os elementos da posição 4 até a final
sublista_4_fim = legumes[4:]
print("Sublista da posição 4 até o final",sublista_4_fim)

sublista_final = legumes
print(sublista_final)
  



 


