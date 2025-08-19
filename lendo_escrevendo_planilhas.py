from pathlib import Path
import pandas as pd
import openpyxl

pasta_atual = Path(__file__).parent

'''
#lendo tabelas com dataframe
tabela_cliente = pd.read_excel(pasta_atual/ 'planilhas'/ 'clientes.xlsx')
print(tabela_cliente.head(10))
'''
'''
#lendo aba específica
tabela_cliente = pd.read_excel(pasta_atual/ 'planilhas'/ 'clientes.xlsx', sheet_name = 'SC')
print(tabela_cliente.head(10))
'''
'''
#modificando header 
tabela_cliente = pd.read_excel(pasta_atual/ 'planilhas'/ 'clientes.xlsx', sheet_name = 'SC', header = 0)
print(tabela_cliente.head(10))
'''
'''
#adicionando coluna de index
tabela_cliente = pd.read_excel(pasta_atual/ 'planilhas'/ 'clientes.xlsx', sheet_name = 'SC', index_col = 0)
print(tabela_cliente.head(10))
'''
'''
#lendo colunas específicas
tabela_cliente = pd.read_excel(pasta_atual/ 'planilhas'/ 'clientes.xlsx', sheet_name = 'SC', usecols =[0, 1])
print(tabela_cliente.head(10))
'''
'''
#comentários sobre decimals e thousands
tabela_cliente = pd.read_excel(pasta_atual/ 'planilhas'/ 'clientes.xlsx', sheet_name = 'SC', decimal='.')
print(tabela_cliente.head(10))
'''
'''
tabela_cliente = pd.read_excel(pasta_atual/ 'planilhas'/ 'clientes.xlsx', sheet_name = 'SC', thousands='.')
print(tabela_cliente.head(10))
'''
'''
#escrevendo planilha
tabela_cliente = pd.read_excel(pasta_atual/ 'planilhas'/ 'clientes.xlsx')
tabela_cliente.to_excel(pasta_atual/ 'planilhas'/ 'copia_clientes.xlsx')
'''

#escrevendo diversas abas
tabela_cliente_rs = pd.read_excel(pasta_atual/ 'planilhas'/ 'clientes.xlsx', sheet_name= 'RS')
tabela_cliente_sc = pd.read_excel(pasta_atual/ 'planilhas'/ 'clientes.xlsx', sheet_name= 'SC')

with pd.ExcelFile(pasta_atual/ 'planilhas'/ 'copia_clientes.xlsx') as nova_planilha:
    tabela_cliente_rs.to_excel(nova_planilha, sheet_name= 'RS', index = False)
    tabela_cliente_sc.to_excel(nova_planilha, sheet_name= 'SC', index = False)
