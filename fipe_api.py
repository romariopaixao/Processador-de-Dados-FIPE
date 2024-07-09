import requests

def retorna_valor_fipe(type_vehicle: str, code_fipe: str, year_car: str):
    r = requests.get(f'https://parallelum.com.br/fipe/api/v2/{type_vehicle}/{code_fipe}/years/{year_car}')
    data = r.json()
    if r.status_code == 200:
        return data['price'], data['referenceMonth']
    else:
        return None, None