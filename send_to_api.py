import requests
import json
from processing_data import *
from login_api import *
import time


# FORNECEDORES
def send_fornecedor(id):
    lista_dados = tratando_fornecedor(id)
    token = login_api()

    #TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/integration/fornecedor/'
    url_valid_test = 'https://insight.ecluster.com.br/api/integration/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    tamanho = len(lista_dados)

    if tamanho > 20:
        n = int(round(len(lista_dados) / 20, 0))
    else:
        n = 1

    dados = [lista_dados[i::n] for i in range(n)]

    response = requests.get(url=url_valid_test, headers=headers)

    if response.status_code == 200:
        for i in dados:            
            data = json.dumps(i)

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)

                print(response.status_code)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# PRODUTOS
def send_produto(id):
    lista_dados = tratando_produto(id)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/integration/produto/'
    url_valid_test = 'https://insight.ecluster.com.br/api/integration/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    tamanho = len(lista_dados)

    if tamanho > 20:
        n = int(round(len(lista_dados) / 20, 0))
    else:
        n = 1

    dados = [lista_dados[i::n] for i in range(n)]

    response = requests.get(url=url_valid_test, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)

                print(response.status_code)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# HISTORICO
def send_historico(id, inicio, fim):
    lista_dados = tratando_historico(id, inicio, fim)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/integration/historico/'
    url_valid_test = 'https://insight.ecluster.com.br/api/integration/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    tamanho = len(lista_dados)

    if tamanho > 20:
        n = int(round(len(lista_dados) / 20, 0))
    else:
        n = 1

    dados = [lista_dados[i::n] for i in range(n)]

    response = requests.get(url=url_valid_test, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)

                print(response.status_code)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# VENDAS
def send_vendas(id, inicio, fim):
    lista_dados = tratando_venda(id, inicio, fim)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/integration/venda/'
    url_valid_test = 'https://insight.ecluster.com.br/api/integration/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    tamanho = len(lista_dados)

    if tamanho > 20:
        n = int(round(len(lista_dados) / 20, 0))
    else:
        n = 1

    dados = [lista_dados[i::n] for i in range(n)]

    response = requests.get(url=url_valid_test, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)

                print(response.status_code)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# ENTRADAS
def send_entrada(id, inicio, fim):
    lista_dados = tratando_entrada(id, inicio, fim)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/integration/entrada/'
    url_valid_test = 'https://insight.ecluster.com.br/api/integration/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    tamanho = len(lista_dados)

    if tamanho > 20:
        n = int(round(len(lista_dados) / 20, 0))
    else:
        n = 1

    dados = [lista_dados[i::n] for i in range(n)]

    response = requests.get(url=url_valid_test, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)

                print(response.status_code)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# PEDIDOS
def send_pedidos(id, inicio, fim):
    lista_dados = tratando_pedido(id, inicio, fim)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/integration/pedido/'
    url_valid_test = 'https://insight.ecluster.com.br/api/integration/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    tamanho = len(lista_dados)

    if tamanho > 20:
        n = int(round(len(lista_dados) / 20, 0))
    else:
        n = 1

    dados = [lista_dados[i::n] for i in range(n)]

    response = requests.get(url=url_valid_test, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)

                print(response.status_code)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')


# ESTOQUE ATUAL
def send_estoque(id):
    lista_dados = tratando_estoque(id)
    token = login_api()

    # TODO URL DA APLICAÇÃO
    url = 'https://insight.ecluster.com.br/api/integration/estoque/'
    url_valid_test = 'https://insight.ecluster.com.br/api/integration/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    tamanho = len(lista_dados)

    if tamanho > 20:
        n = int(round(len(lista_dados) / 20, 0))
    else:
        n = 1

    dados = [lista_dados[i::n] for i in range(n)]
    response = requests.get(url=url_valid_test, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)

            try:
                response = requests.post(url=url, headers=headers, data=data)
                print(response.status_code)

            except requests.ConnectionError:
                print("SEM CONEXÃO COM O SERVIDOR")
                print("RECONECTANDO EM 150 SEGUNDOS")

                time.sleep(150)

                response = requests.post(url=url, headers=headers, data=data)

                print(response.status_code)

        return response.status_code
    else:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')
