# README - Web Scraping da Plataforma Sucupira

## Descrição do Projeto

Este script realiza web scraping da plataforma Sucupira para extrair ementas de disciplinas de programas de pós-graduação. O objetivo é catalogar as soft e hard skills presentes nas disciplinas, permitindo uma análise posterior sobre sua aplicação na formação dos pós-graduados. O código foi otimizado para funcionar sem Selenium, utilizando apenas `requests` e `BeautifulSoup` para acessar os dados via API.

## Requisitos

Antes de executar o script, certifique-se de que sua máquina possui os seguintes itens instalados:

- Python 3.9 ou superior
- Pacotes Python:
  - `requests`
  - `pandas`
  - `json`

Para instalar os pacotes necessários, execute:
```sh
pip install requests pandas
```

## Como Executar o Script

1. **Baixe e prepare o arquivo CSV**
   - O script analisa um arquivo CSV contendo os links dos programas de pós-graduação.
   - Atualize o caminho do arquivo no parâmetro `file_path` dentro do script.

2. **Execute o script**
   - Abra um terminal ou prompt de comando e navegue até o diretório onde o script está salvo.
   - Execute o seguinte comando:
     ```sh
     python nome_do_script.py
     ```

## Saídas do Script

O script gera três arquivos principais:

1. **`disciplinas_coletadas.csv`** - Contém os dados extraídos, incluindo nome do programa, nome da instituição, sigla da instituição, nome da disciplina e sua ementa.
2. **`disciplinas_coletadas.json`** - Versão JSON dos dados coletados.
3. **`errors_log.csv`** - Lista de disciplinas que não puderam ser acessadas, caso existam erros na execução.

Se não houver erros, o arquivo `errors_log.csv` não será gerado.

## Personalização

- Para modificar o intervalo de leitura do arquivo CSV, altere os parâmetros da função `pd.read_csv()`. Atualmente, o script está configurado para ler um intervalo específico:
  ```python
  df = pd.read_csv(file_path, skiprows=500, nrows=100, header=None)
  ```
  - `skiprows=500`: Pula as primeiras 500 linhas.
  - `nrows=100`: Lê apenas 100 linhas após o intervalo ignorado.

- Para coletar desde o início do arquivo, utilize:
  ```python
  df = pd.read_csv(file_path, nrows=50)
  ```

## Contato

Autora: **Mayara Silva**  
Projeto desenvolvido para o **No Budget Science Hack Week**.  
Caso tenha dúvidas ou precise de suporte, entre em contato!

