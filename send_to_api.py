import requests
import json
from processing_data import *
from login_api import *


# FORNECEDOR
def send_fornecedor():
    dados = tratando_fornecedor()
    token = login_api()

    #TODO URL DA APLICAÇÃO
    url = 'http://177.136.201.66/api/fornecedor/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
            print(response.status_code, response.text)
            print(data)
        return response.status_code
    else:
        token = login_api()


# PRODUTOS
def send_produto():
    dados = tratando_produto()
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'http://177.136.201.66/api/produto/'
    headers = {
        'Authorization': token,
        'content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
            print(response.status_code, response.text)
            print(data)
        return response.status_code
    else:
        token = login_api()


# ESTOQUE ATUAL
def send_estoque():
    dados = tratando_estoque()
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'http://177.136.201.66/api/estoque-atual/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
            print(response.status_code, response.text)
            print(data)
        return response.status_code
    else:
        token = login_api()


# PEDIDOS
def send_pedidos():
    dados = tratando_pedidos()
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'http://177.136.201.66/api/pedido-compra/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    response = requests.get(url=url, headers=headers)


    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
            print(response.status_code, response.text)
            print(data)
        return response.status_code
    else:
        token = login_api()


# ENTRADAS
def send_entrada():
    dados = tratando_entrada()
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = "http://177.136.201.66/api/ultima-entrada/"
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
            print(response.status_code, response.text)
            print(data)
        return response.status_code
    else:
        token = login_api()


#VENDAS
def send_vendas():
    dados = tratando_venda()
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = "http://177.136.201.66/api/venda/"
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
            print(response.status_code, response.text)
            print(data)
        return response.status_code
    else:
        token = login_api()


# HISTORICO
def send_historico():
    dados = tratando_historico()
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'http://177.136.201.66/api/historico-estoque/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    response = requests.get(url=url, headers=headers)


    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
            print(response.status_code, response.text)
            print(data)
        return response.status_code
    else:
        token = login_api()