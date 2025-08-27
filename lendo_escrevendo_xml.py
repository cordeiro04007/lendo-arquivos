import xml.dom.minidom
from pathlib import Path

pasta_atual = Path(__file__).parent
#lendo arquivo xml
domtree = xml.dom.minidom.parse(str(pasta_atual/ 'xmls'/ 'livros.xml'))
group = domtree.documentElement
livros = group.getElementsByTagName('livro')
#print(group)
#print(len(livros))

#interando por elementos e retornando valores
'''
for livro in livros:
    titulo = livro.getElementsByTagName('titulo')[0].childNodes[0].nodeValue
    print(titulo)

for autores in livros:
    autor = autores.getElementsByTagName('autor')[0].childNodes[0].nodeValue
    print(autor)

for precos in livros:
    preco = precos.getElementsByTagName('preco')[0].childNodes[0].nodeValue
    print(preco)

for data_publicacao in livros:
    data = data_publicacao.getElementsByTagName('data_publicacao')[0].childNodes[0].nodeValue
    print(data)
'''
#salvando um arquivo xml
livros[0].getElementsByTagName('autor')[0].childNodes[0].nodeValue = 'Cordeiro, Alex'

with open(pasta_atual/ 'xmls'/ ' livros_copia.xml', 'w') as f:
    domtree.writexml(f)

