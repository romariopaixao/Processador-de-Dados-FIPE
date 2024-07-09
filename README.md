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

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests ou abrir issues para sugerir melhorias ou reportar bugs.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
