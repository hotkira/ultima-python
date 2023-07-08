import sqlite3
from requests_html import HTMLSession
sessao = HTMLSession()
url = 'https://www.olx.com.br/imoveis/aluguel/estado-pr/regiao-de-maringa/'
resposta = sessao.get(url)
imoveis = []
for link in resposta.html.find("#ad-list li a"):
    url_imovel = link.attrs['href']
    resposta_imovel = sessao.get(url_imovel)
    titulo = resposta_imovel.html.find('h1', first=True).text
    preco = resposta_imovel.html.find('h2')[6].text
    imoveis.append({
        'url': url_imovel,
        'titulo' : titulo,
        'preco' : preco
    })
    #print('url: ',url_imovel)
    #print('titulo: ',titulo)
    #print('preco: ',preco)

conexao = sqlite3.connect('banco_raspagem.sqlite3')
cursor=conexao.cursor()
sql = 'insert into imovel (url, titulo, preco) values (?, ?, ?)'
for imovel in imoveis:
    valores = [imovel['url'], imovel['titulo'], imovel['preco']]
    cursor.execute(sql, valores)

conexao.commit()
conexao.close()