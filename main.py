from send_to_api import *
from login_api import *

def execute_main():
    send_fornecedor()
    send_produto()
    send_entrada()
    send_estoque()
    send_pedidos()
    send_historico()
    send_vendas()
    print("INTEGRAÇÃO CONCLUIDA COM SUCESSO!")

if __name__ == '__main__':
    print('ta funcionando')
    execute_main()
