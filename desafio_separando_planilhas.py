from pathlib import Path
import pandas as pd
import os
import shutil

pasta_atual = Path(__file__).parent

def criar_pasta(caminho):
  """
  Cria uma pasta no caminho especificado.

  Args:
    caminho: O caminho completo ou relativo da pasta a ser criada.
  """
  if not os.path.exists(pasta_atual/ 'planilhas' / caminho):
    os.makedirs(caminho)
    print(f"Pasta criada em: {caminho}")
  else:
    print(f"A pasta já existe em: {caminho}")

def movendo_pastas (mover_pasta = ''):
    pasta_atual = Path(__file__).parent
    caminho_pasta = pasta_atual / mover_pasta
    caminho_pasta_destino = pasta_atual/ 'planilhas'  /  mover_pasta
    if os.path.exists(caminho_pasta):
        if not os.path.isdir(caminho_pasta_destino):
            shutil.move(caminho_pasta, caminho_pasta_destino)

# Exemplo de uso:
caminho_pasta = "planilha_consolidada"  # Pode ser um caminho absoluto ou relativo
criar_pasta(caminho_pasta)
movendo_pastas(mover_pasta=caminho_pasta)

#############################################################################################

def separando_planilhas(arquivo_novo='', nome_aba=''):
    tabela_cliente = pd.read_excel(pasta_atual/ 'planilhas'/ 'clientes.xlsx', sheet_name= nome_aba)
    tabela_cliente.to_excel(pasta_atual/ 'planilhas'/'planilhas_separadas'/ arquivo_novo)

    with pd.ExcelFile(pasta_atual/ 'planilhas'/'planilhas_separadas'/ arquivo_novo) as nova_planilha:
        tabela_cliente.to_excel(nova_planilha, sheet_name= nome_aba, index = False)
separando_planilhas(arquivo_novo = 'SP.xlsx', nome_aba='SP')

#############################################################################################

pasta_separadas = pasta_atual / 'planilhas' / 'planilhas_separadas'
pasta_consolidada = pasta_atual / 'planilhas'/ 'planilha_consolidada'



def consolidando_planilhas(pasta_separadas):
  with pd.ExcelWriter(pasta_consolidada/ 'clientes.xlsx') as consolidada:
     for arquivo in Path(pasta_separadas).glob('*.xlsx'):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidada, sheet_name= arquivo.stem, index= False)

consolidando_planilhas(pasta_separadas)