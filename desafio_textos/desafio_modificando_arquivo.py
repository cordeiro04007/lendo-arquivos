from pathlib import Path

item_remover = 'Passear com cachorro'

pasta_atual = Path(__file__). parent

pasta_c_arquivos_html = pasta_atual / 'desafio_textos'

with open(pasta_atual / 'view_lista.html') as visualizar_lista_html:
    itens_visualizar = visualizar_lista_html.readlines()

novas_linhas_html = []
escrever_linha = True

for i, linha in enumerate(itens_visualizar):

    if i < len(itens_visualizar) -3 and item_remover in itens_visualizar[i+2]:
        escrever_linha = False
    
    if escrever_linha:
        novas_linhas_html.append(linha)
        
    if '</li>' in linha:
        escrever_linha = True

with open(pasta_atual / 'view_lista_atualizada.html', mode = 'w') as view_lista_atualizada:
    for item in novas_linhas_html:
        view_lista_atualizada.write(item)
            


         






