import requests
import json
from processing_data import *
from login_api import *
import time


# FORNECEDORES
def send_fornecedor(id):
    dados = tratando_fornecedor(id)
    token = login_api()

    #TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/fornecedor/'
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

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# PRODUTOS
def send_produto(id):
    dados = tratando_produto(id)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/produto/'
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

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# HISTORICO
def send_historico(id, inicio, fim):
    dados = tratando_historico(id, inicio, fim)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/historico-estoque/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    response = requests.get(url=url, headers=headers)

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# VENDAS
def send_vendas(id, inicio, fim):
    dados = tratando_venda(id, inicio, fim)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = "https://insight.ecluster.com.br/api/venda/"
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

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# ENTRADAS
def send_entrada(id, inicio, fim):
    dados = tratando_entrada(id, inicio, fim)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = "https://insight.ecluster.com.br/api/ultima-entrada/"
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

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# PEDIDOS
def send_pedidos(id, inicio, fim):
    dados = tratando_pedidos(id, inicio, fim)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/pedido-compra/'
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

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# ESTOQUE ATUAL
def send_estoque(id):
    dados = tratando_estoque(id)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/estoque-atual/'
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

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code, response.text)
                print(data)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')
