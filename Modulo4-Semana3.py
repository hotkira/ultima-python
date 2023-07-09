#Imkporta a biblioteca HTMLSession da biblioteca requests_html
from requests_html import HTMLSession
#cria a sessão HTML usando aclasse HTMLSession
sessao = HTMLSession()
#Define a url a ser acessada
url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'
# Faz uma requisição GET à página da web usando a sessão criada
resposta = sessao.get(url)
# Criauma lista vazia para armazenar as informações do anuncio
anuncios = []
#Usa o método find do objeto html retornado na resposta para encontrar todososlinks
links = resposta.html.find('#ad-list li a')
# Itera sobre todos os links encontrados na página
for link in links:
    # Extrai o link de cada produto 
    url_iphone = link.attrs['href']
    # Fazuma requisição SET na URL de cada anuncio usando a sesso criada
    resposta_iphone = sessao.get(url_iphone)
    
    # Extrai o titulo e o preço
    titulo = resposta_iphone.html.find('h1', first=True).text
    h2_elementos = resposta_iphone.html.find('h2')
    
    #dando print,  descobri que na posição [6], varia entre R$ e o valor
    #então fiz um if alternando nas duas posições para extrair o valor
    
    
    if h2_elementos[6].text == "R$":
        preco = h2_elementos[7].text
    else:
    # Define um valor padrão caso o atributo não esteja presente
        preco = h2_elementos[6].text
        
    
    #Adiciona as informações do anuncio na lista de anuncios
    anuncios.append({
        'url': url_iphone,
        'titulo': titulo,
        'preco': preco
        
    })
    
    
    #imprime alista
    print(anuncios)