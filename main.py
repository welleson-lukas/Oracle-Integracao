from send_to_api import *
from login_api import *


def execute_main():
    send_fornecedor()
    send_produto()
    send_historico()
    send_vendas()
    send_entrada()
    send_pedidos()
    send_estoque()

    print("INTEGRAÇÃO CONCLUIDA COM SUCESSO!")


if __name__ == '__main__':
    execute_main()
