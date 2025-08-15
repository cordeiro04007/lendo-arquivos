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
'''
#LENDO LINHA A LINHA
pasta_atual = Path(__file__).parent

with open(pasta_atual / 'lista_de_compras.txt') as lista_de_compras:
    linha = lista_de_compras.readline()
    while linha != '':
        print(linha,end = '')
        linha = lista_de_compras.readline()
'''


'''
# LENDO TODAS AS LINHAS
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'lista_de_compras.txt') as lista_de_compras:
    print(lista_de_compras.readlines())
'''

'''
#ESCREVENDO ARQUIVO
pasta_atual = Path(__file__).parent

itens_ja_comprados =['farinha', 'fermento', 'agua']

with open(pasta_atual / 'lista_de_compras.txt') as lista_de_compras:
        itens_lista = lista_de_compras.readlines()

with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode = 'w') as lista_atualizada:
        for item in itens_lista:
            if not item.replace('\n', '') in itens_ja_comprados:
                   lista_atualizada.write(item)
'''

'''

# ESCREVENDO LINHA A LINHA
pasta_atual = Path(__file__).parent

itens_ja_comprados =['farinha', 'fermento', 'agua']

with open(pasta_atual / 'lista_de_compras.txt') as lista_de_compras:
        itens_lista = lista_de_compras.readlines()

itens_lista_atualizada = []
for item in itens_lista:
        if not item.replace('\n', '') in itens_ja_comprados:
            itens_lista_atualizada.append(item)
with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode = 'w') as lista_atualizada:
       itens_lista_atualizada [-1] = itens_lista_atualizada [-1].replace('\n', '')

       lista_atualizada.writelines(itens_lista_atualizada)        
'''

# ACRESCENTANDO VALORES A UM ARQUIVO
pasta_atual = Path(__file__).parent
novos_itens = ['abacate']

novos_itens_c_quebra = []

for item in novos_itens:
    novos_itens_c_quebra.append(f'\n{item}')
with open(pasta_atual / 'lista_de_compras.txt', mode = 'a') as lista_adicionada:
    lista_adicionada.writelines(novos_itens_c_quebra)
