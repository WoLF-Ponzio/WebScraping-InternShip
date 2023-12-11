import requests

url = 'http://localhost:3000/vagas'

def test_requisicao_ok():
    response = requests.get(url)
    assert response.status_code == 200

def test_requisicao_falha():
    response = requests.get(url)
    assert response.status_code != 200

