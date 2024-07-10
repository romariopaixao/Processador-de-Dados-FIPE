# Processador de Dados FIPE

## Introdução

Este projeto consiste em um conjunto de scripts Python que automatizam o processo de obtenção de valores de veículos da Tabela FIPE. O sistema recebe uma planilha contendo dados de placas e códigos da tabela FIPE, consulta a API da FIPE para cada veículo e gera uma nova planilha com os valores atualizados e a data de referência.

## Funcionalidades

- Lê dados de veículos de uma planilha Excel
- Consulta a API da FIPE para obter valores atualizados
- Gera uma nova planilha com os valores e datas de referência

## Pré-requisitos

Antes de executar o script, certifique-se de ter instalado:

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/processador-dados-fipe.git
   cd processador-dados-fipe
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Estrutura do Projeto

- `fipe_api.py`: Contém a função para fazer requisições à API da FIPE
- `data_processor.py`: Contém a lógica para processar os dados da planilha
- `main.py`: Script principal que executa todo o processo
- `requirements.txt`: Lista de dependências do projeto

## Como Usar

1. Prepare sua planilha de entrada com o nome "FIPE_API.xlsx" no mesmo diretório do script.

2. Execute o script principal:
   ```
   python main.py
   ```

3. O script processará os dados e gerará um novo arquivo Excel com o nome "FIPE_API_[MÊS].xlsx", onde [MÊS] é o mês atual.

## Formato da Planilha de Entrada

Para garantir o funcionamento correto do script, sua planilha de entrada (FIPE_API.xlsx) deve seguir o seguinte formato:

| PLACA | cod fipe | ano  | tipo     |
|-------|----------|------|----------|
| ABC1234 | 001303-0 | 2020 | cars     |
| XYZ5678 | 021231-7 | 2019 | trucks   |

- PLACA: A placa do veículo
- cod fipe: O código FIPE do veículo
- ano: O ano do veículo
- tipo: O tipo de veículo (cars, trucks, motorcycles)

Certifique-se de que os nomes das colunas estejam exatamente como mostrado acima, incluindo maiúsculas e minúsculas.

## Solução de Problemas

Se o script apresentar erros, verifique se:

1. Os nomes das colunas na sua planilha de entrada estão exatamente como especificado acima.
2. Não há células vazias nas colunas necessárias.
3. O arquivo da planilha está no formato .xlsx e não .xls ou outro formato.

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests ou abrir issues para sugerir melhorias ou reportar bugs.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
