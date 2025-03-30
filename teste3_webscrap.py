### data: 20 nov 2024
### script para o projeto No Budget Science Hack Week - webscraping da página Sucupira
## ação: analisar cada programa de pós e imprimir as ementas
### autora: Mayara Silva 
### última atualização: 16 mar 2025

#### ETAPA: Código ADAPTADO para a versão SEM SELENIUM.
#### STATUS: O código está REVISADO, funcionando sem selenium e agora está imprimindo as disciplinas com as EMENTAS para CSV e JSON!
### A planilha de erros não é impressa se estiver em branco!

import requests
import pandas as pd
import json
import time

session = requests.Session()

# Caminho do arquivo CSV de entrada
file_path = r'C:\Users\mayar\Downloads\Estudos\webdriver_att\20240912_nbshw_extracted_links_test.csv' #ALTERAR CAMINHO
#df = pd.read_csv(file_path, nrows=50) # Desde o início
df = pd.read_csv(file_path, skiprows=900, nrows=147, header=None) # De intervalo x a y

# Listas para armazenar dados e erros
disciplinas_coletadas = []
errors = []

def get_disciplina_data(disciplina_id, programa_id):
    """Acessa a API de disciplina individual e retorna os dados."""
    api_url = f"https://sucupira.capes.gov.br/api/data/observatorio/disciplina/{disciplina_id}"
    response = session.get(api_url)
    
    if response.status_code == 200:
        time.sleep(2)
        return response.json()
    else:
        print(f"Erro ao acessar a disciplina {disciplina_id}. Programa ID associado: {programa_id}")
        errors.append((disciplina_id, programa_id))  
        return None

# Loop pelas URLs no arquivo CSV
for _, row in df.iterrows():
    # Desde o início
    #url = row['href']
    #ano_base = row['AN_BASE']

    # De intervalo x a y
    url = row[0]
    ano_base = row[3]
    programa_id = url.split('programas/')[-1].split('?')[0]

    # Paginação da API
    page = 0
    while True:
        api_url = f"https://sucupira.capes.gov.br/api/data/observatorio/disciplina?page={page}&size=100&query=id-programa:({programa_id})%3Bano-base:({ano_base})"
        response = session.get(api_url)
        
        if response.status_code != 200:
            print(f"Erro ao acessar API para programa {programa_id}, ano base {ano_base}, página {page}")
            break

        data = response.json()
        
        # Coletar IDs das disciplinas
        for item in data.get('content', []):
            disciplina_id = item.get('id')
            if disciplina_id:
                disciplina_data = get_disciplina_data(disciplina_id, programa_id)
                if disciplina_data:
                    disciplinas_coletadas.append([
                        disciplina_data.get('nomePrograma', ''),
                        disciplina_data.get('nomeIes', ''),
                        disciplina_data.get('siglaIes', ''),
                        disciplina_data.get('nomeDisciplina', ''),
                        disciplina_data.get('ementaDisciplina', '')
                    ])
        
        if len(data['content']) < 100:
            break
        page += 1
        time.sleep(2)

# Exportar dados coletados para CSV
output_csv = r'C:\Users\mayar\Downloads\Estudos\webdriver_att\disciplinas_coletadas.csv' #ALTERAR CAMINHO
df_coletadas = pd.DataFrame(disciplinas_coletadas, columns=['nomePrograma', 'nomeIes', 'siglaIes', 'nomeDisciplina', 'ementaDisciplina'])
df_coletadas.to_csv(output_csv, index=False)

# Exportar dados para JSON
output_json = r'C:\Users\mayar\Downloads\Estudos\webdriver_att\disciplinas_coletadas.json' #ALTERAR CAMINHO
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(disciplinas_coletadas, f, ensure_ascii=False, indent=4)

print(f"Dados exportados para {output_csv} e {output_json}")

# Exportar erros para um CSV somente se houver erros
if errors:
    errors_df = pd.DataFrame(errors, columns=['disciplina_id', 'programa_id'])
    errors_csv = r'C:\Users\mayar\Downloads\Estudos\webdriver_att\errors_log.csv' #ALTERAR CAMINHO
    errors_df.to_csv(errors_csv, index=False)
    print(f"Erros exportados para {errors_csv}")

