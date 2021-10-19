url = "https://www.byte bank.com/cambio?moed aOrigem=real&moedaDesti no=dolar"

#Sanitização dos dados
url = url.replace(" ", "")
print(url)

#O metodo find retorna o index da posição do caractere passado como parametro

# search_query = url[interrogacao_index + 1:]

search_param = 'moedaOrigem'

param_index = url.find(search_param)

e_comercial_index = url.find('&', param_index)

equal_index = param_index + len(search_param)

if (e_comercial_index == -1):
    print(url[param_index:])
else:
    print(url[param_index:e_comercial_index])


class Extractor_URL:
    def __init__(self, url):
        self.url = self.__sanitaze_url(url)
    
    def __sanitaze_url(self, url):
        return url.strip()

    @property
    def domain_site(self):
        interrogacao_index = self.url.find('?')
        site_domain = self.url[:interrogacao_index]
        return site_domain
    
bytebank = Extractor_URL(url)
print(bytebank.domain_site)