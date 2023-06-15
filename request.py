import requests

data = {
    'accion': 'AMZN',
    'fecha_inicial': '2023-01-01',
    'fecha_final': '2023-06-01'
}

response = requests.post('http://localhost:5000/', json=data)
print(response.json())
