from pathlib import Path

pasta_atual = Path(__file__). parent


pasta_c_arquivos_html = pasta_atual / 'desafio_textos'

itens_na_view_lista = ['Almoçar', 'Passear com cachorro', 'Ir ao shopping']

with open(pasta_atual / 'view_lista.html') as visualizar_lista_html:
    itens_visualizar = visualizar_lista_html.readlines()

with open(pasta_atual / 'view_lista_atualizada.html', mode = 'w') as view_lista_atualizada:
    for item in itens_visualizar:
        itens_na_view_lista.append(view_lista_atualizada)
        
        view_lista_atualizada.write(item)




