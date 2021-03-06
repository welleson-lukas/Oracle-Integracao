import requests


def login_api():
    usuario = 'cluster'
    senha = 'Cluster*2018'

    url = "https://insight.ecluster.com.br/api-token-auth"
    #url = "http://127.0.0.1:8000/api-token-auth"
    user_data = {
        "username": usuario,
        "password": senha
    }

    try:
        response = requests.post(url=url, json=user_data)

        if response.status_code == 200:
            response_data = response.json()
            token_puro = response_data['token']

            token = "Token "
            token += token_puro
            print(token)
            return token

    except requests.ConnectionError:
        print('NÃO FOI POSSÍVEL CONECTAR AO SERVIDOR')
