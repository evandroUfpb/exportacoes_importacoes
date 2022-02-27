import requests
from urllib3.exceptions import InsecureRequestWarning


# funções par baixar os arquivos com dados das exportações e importações 
# para os anos de 2012 a 2021
# salva os arquivos em um subdiretório 'dados'

def baixar_arquivos_exp(url, filename):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True, verify=False)
    if r.status_code == 200:
        with open("dados/"+filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)                    
                    f.flush()                    
        print(f'arquivo EXP_{ano}.csv importado')            
    else:
        print("Arquivo não encontrado!")
    return local_filename    

def baixar_arquivos_imp(url, filename):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True, verify=False)
    if r.status_code == 200:
        with open("dados/"+filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        print(f'arquivo IMP_{ano}.csv importado')            
    else:
        print("Arquivo não encontrado!")
    return local_filename



if __name__ == "__main__":
    
    anos = list(str(i) for i in range(2014, 2022))
    for ano in anos:
        url = f'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_{ano}.csv'
        filename = f"EXP_{ano}.csv"
        baixar_arquivos_exp(url, filename)
    
        url2 = f'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/IMP_{ano}.csv'
        filename2 = f"IMP_{ano}.csv"
        baixar_arquivos_imp(url=url2, filename=filename2)
    