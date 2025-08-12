from pathlib import Path
import shutil
'''
# LENDO UM ARQUIVO FORMA NÃO RECOMENDADA
pasta_atual = Path(__file__).parent

lista_de_compras = open(pasta_atual / 'lista_de_compras.txt')

print(lista_de_compras.read())

lista_de_compras.close()
'''


'''
# LENDO ARQUIVO FORMA RECOMENDADA
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt') as lista_de_compras:
    print(lista_de_compras.read())
'''

#LENDO LINHA A LINHA
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt') as lista_de_compras:
    linha = lista_de_compras.readline()
    while linha != '':
        print(linha,end = '')
        linha = lista_de_compras.readline()


# LENDO TODAS AS LINHAS


#ESCREVENDO ARQUIVO


# ESCREVENDO LINHA A LINHA


# ACRESCENTANDO VALORES A UM ARQUIVO

