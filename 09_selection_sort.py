# Variáveis de contagem

comps = trocas = passd = 0

def selection_sort(lista):
    """
    ALGORTIMO DE ORDENAÇÃO SELECTION SORT
    Isola (seleciona) o primeiro elemento da lista e , em seguida,
    encontra o menor valor do restante da lista. Se o valor encontrado for menor 
    que o valor previamente selecionado, efetua a troca entre elas, continuando, seleciona
    o segundo elemento da lista, buscando pelo menor valor nas posições subsequentes. Faz a troca
    entre os dois valores, se necessário, o processo se repete até que o penultimo elemento da lista
    seja selecionado, comparado com o último e feita a troca entre eles se for o caso
    """
    global comps, trocas, passd 
    comps = trocas = passd = 0

    # Loop que vai da primeira até a penultima posição, para
    # selecionar o elemento que será comparado dos demais

    for pos_sel in range(len(lista) - 1):
        passd += 1
        # inicia supondo que a posição do menor valor do resto
        #  da lista é o que está imediatamente a frente do selecionado
        pos_menor = pos_sel + 1

        # percorre o restante da lista, da posição seguinte a pos_menor
        # até a última posição

        for pos in range (pos_menor + 1, len(lista)):
            # se o valor encontrado na posição pos for MENOR do que o
            # valor atual de pos_menor, então atualiza pos_menor para
            # a mesma posição de pos

            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos 
        # <- CUIDADO COM A IDENTAÇÃO
        # Neste ponto já terminamos de percorrer o restante da lista e 
        # já sabemos a posição do menor elemento que há nele, comparamos 
        #  então, os valores das posições pos_menor e pos_sel, se o 
        #  primeiro for MENOR do que o segundo, fazemos a troca entre eles
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1
###################################################################################################
# 
#nums = [7,5,9,0,3,4,8,1,6,2]
# pior caso 
#nums = [9,8,7,6,5,4,3,2,1,0]
nums = [1,2,3,4,5,6,7,8,9,0]
# melhor caso
#nums = [0,1,2,3,4,5,6,7,8,9] #
"""
passadas:n-1(constante)
comparações:((n^2)-n)/2
trocas:n - 1
"""


print ("Antes: ",nums)
selection_sort(nums)   
print("Depois: ",nums)
print(f"Passadas:{passd}; comparações: {comps}; trocas: {trocas} " ) 

#####################################################################################

import sys
sys.dont_write_bytecode = True # Impede a criação do cache
from time import time

#Importando a lista de nomes

from data.nomes_desord import nomes

nomes = nomes[:10000]

hora_ini = time()
selection_sort(nomes)
hora_fim = time()
print(nomes) # Lista após ordenação
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Passadas: {passd}; Comparações: {comps}; Trocas: {trocas}")
