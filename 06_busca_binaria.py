"""
Algortimo de busca binária 

dados uma lista, que deve estar previamente ordenada, e um valor de busca, divide a lista em duas partes
procurando pelo valor de busca apenas na metade onde o valor de busca poderia estar,novas subdivisões
são feitas até que se encontre o valor de busca ou que reste apenas uma sublista vazia, quando então se
conclui que o valor de busca não existe na lista

"""

comps = 0

def busca_binaria(lista,val):
 global comps
 comps = 0
 ini = 0            # Posição inicial da variável

 fim = len(lista)-1 # Posição final da lista

 while ini <= fim:
    #calculando o meio da lista
    meio = (ini + fim) // 2 #divisão inteira

# Verifica se o valor que está no meio da lista
# é igual ao valor de busca. Em caso afirmativo,
# retornamos a posição do meio, pois o valor de busca não foi encontrado

    if val == lista[meio]:
        comps += 1
        return meio
    
    # Senão se o valor de busca é menor, do que o valor
    #Valor do meio, reinicia a busca na metade esquerda
    # da sublista
    elif val < lista[meio]:
        comps += 2
        fim = meio -1
    # Por fim, se o valor de busca é MAIOR do que o  
    # valor do meio, reinicia a busca na metade direita
    # da sublista
    else:
        comps += 2
        ini = meio + 1
# <- cuidado com a identação aqui
#
#
#
# 

 return -1

#############################################################################


import sys
sys.dont_write_bytecode = True

from time import time

# TESTES COM NOMES
from data.nomes_completos import nomes

hora_ini = time()
resultado1 = busca_binaria(nomes, "EDSON PEREIRA")
hora_fim = time()
print(f"EDSON PEREIRA encontrado na posição {resultado1}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Comparações: {comps}")

hora_ini = time()
resultado2 = busca_binaria(nomes, "MARIA FERREIRA")
hora_fim = time()
print(f"MARIA FERREIRA encontrado na posição {resultado2}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Comparações: {comps}")
###########################################################

hora_ini = time()
resultado3 = busca_binaria(nomes, "VALDIR SILVA")
hora_fim = time()
print(f"VALDIR SILVA encontrado na posição {resultado3}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Comparações: {comps}")
############################################################

hora_ini = time()
resultado4 = busca_binaria(nomes, "GILCINEIA GARCIA")
hora_fim = time()
print(f"GILCINEIA GARCIA encontado na posição {resultado4}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Comparações: {comps}")

###############################################################