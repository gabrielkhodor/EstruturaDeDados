# Variáveis de contagem
comps = trocas = passd = 0 

def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    PERCORRE A LISTA A SER ORDENADA EM SUCESSIVAS PASSADAS,
    trocando entre si dois elementos adjacentes. Efetua tantas passadas
    quanto necessárias, até que, na última passada, nenhuma troca tenha sido feita 
    
    """
    global comps, trocas, passd
    comps = trocas = passd = 0
    # loop eterno; não sabemos antecipadamente quantas passadas
    # serão necessárias,
    while True:
        passd += 1
        # variável que controla se houve trocas na passada
        trocou = False

        # Percurso da lista, so primeiro ao PENULTIMO  elemento,
        # com acesso a cada posição 

        for pos in range(len(lista)- 1):

            # Se o valor que está a frente na lista (pos +1 )
            # for menor do que aquele que está atrás (pos),
            # efetuamos uma TROCA
            comps += 1
            if lista[pos + 1] < lista[pos]:
                #troca
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocas += 1
                trocou = True # houve troca na passada
        print(lista)        
        # se não houver trocas no passada, a lista está ordenada
        # e interrompemos o loop eterno while true
        if not trocou:
            break

##############################################################################


nums = [7,5,9,0,3,4,8,1,6,2]
#nums = [9,8,7,6,5,4,3,2,1,0]
#nums = [0,1,2,3,4,5,6,7,8,9]
print ("Antes: ",nums)
bubble_sort(nums)   
print("Depois: ",nums)
print(f"Passadas:{passd}; comparações: {comps}; trocas: {trocas} " )

exit() #termina o programa aqui
#################################
"""
PIOR CASO
passadas = n
comparações = n^2 -n 
troca = ((n ^ 2) - n) / 2

MELHOR CASO
passadas = 1
comparações = n - 1
trocas = 0

"""
####################################################################################
# TESTE COM 1M+ DE NOMES

import sys
sys.dont_write_bytecode = True # Impede a criação do cache
from time import time

#Importando a lista de nomes

from data.nomes_desord import nomes

nomes = nomes[:1000]

hora_ini = time()
bubble_sort(nomes)
hora_fim = time()
print(nomes) # Lista após ordenação
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Passadas: {passd}; Comparações: {comps}; Trocas: {trocas}")
