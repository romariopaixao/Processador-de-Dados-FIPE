import pandas as pd
from datetime import datetime
from fipe_api import retorna_valor_fipe

def process_data(input_file: str):
    df = pd.read_excel(input_file, sheet_name='Planilha1')
    
    df['Preco_API'] = ''
    df['Mes_Referencia_API'] = ''

    for indice, linha in df.iterrows():
        placa = linha['PLACA']
        codFipe = linha['cod fipe']
        ano = linha['ano']
        type_vehicle = linha['tipo']

        preco, mes_referencia = retorna_valor_fipe(type_vehicle, codFipe, ano)

        df.at[indice, 'Preco_API'] = preco
        df.at[indice, 'Mes_Referencia_API'] = mes_referencia

        print(f'{placa} feito !')

    nome_mes_atual = datetime.now().strftime('%B')
    output_file = f"FIPE_API_{nome_mes_atual}.xlsx"
    df.to_excel(output_file, index=False)
    
    return output_file