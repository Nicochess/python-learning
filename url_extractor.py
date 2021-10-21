import re

url = "https://www.byte bank.com.br/cambio?moed aOrigem=real&moedaDesti no=dolar"

#Sanitização dos dados
url = url.replace(" ", "")
print(url)

#O metodo find retorna o index da posição do caractere passado como parametro

class Extractor_URL:
    def __init__(self, url):
        self.url = self.__sanitaze_url(url)
        self.validate_url()
    
    def __sanitaze_url(self, url):
        return url.strip()
    
    def get_param(self, param):
        param_index = self.url.find(param)
        comercial_e = self.url.find('&', param_index)
        if comercial_e == -1:
            param_value = self.url[param_index:]
        else:
            param_value = self.url[param_index : comercial_e]
        return param_value
    
    def validate_url(self):
        if not self.url:
            raise ValueError('URL não pode estar vazia')
        
        url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = url_pattern.match(self.url)
        
        if not match:
            raise ValueError('URL é invalida.')
        else:
            print(match)

    @property
    def domain_site(self):
        interrogacao_index = self.url.find('?')
        site_domain = self.url[:interrogacao_index]
        return site_domain
    
bytebank = Extractor_URL(url)
print(bytebank.domain_site)
print(bytebank.get_param("moedaDestino"))