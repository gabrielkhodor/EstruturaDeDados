def busca_sequencial(lista,val):

    """
    Função que realiza uma busca sequencial em uma lista,
    procurando por val.
    Se val for encontrado, retorna a posição de val na lista.
    Caso contrário volta valor convencional -1    
    
    """

    #Percorre a lista do inicio ao fim usando range() e len()
    #(é necessário ter acesso a posição dos elementos)

    for pos in range(len(lista)):
        #encontrou val: retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    # <-- cuidado com a identação aqui!
    #Percorreu toda a lista e não encontrou val: retorno -1
    return -1

    #####################################################################

    #lista de números para testar

    nums = [9,21,33,12,0,18,-3,30,-15,6,3,27]

    #testes

    pos30 = busca_sequencial(nums,30)
    print(f"Elemento 30 encontrado na posição {pos30}")

    pos_menos15 = busca_sequencial(nums,-15)
    print(f"Elemento -15 encontrado na posição {pos_menos15}")

    pos19 = busca_sequencial(nums,19)
    print(f"Elemento 19 encontrado na posição {pos19}")


##########################################################
"""
import sys 
sys.dont_write_bytecode = True

from time import time

#testes com nomes

from data.nomes_completos import nomes

resultado1 = busca_sequencial(nomes,"EDSON PEREIRA")
print(f"EDOSON PEREIRA encontrado na posição ,{resultado1}" )

resultado2 = busca_sequencial(nomes,"MARTA PEREIRA")
print(f"MARTA PEREIRA encontrado na posição {resultado2}")
"""