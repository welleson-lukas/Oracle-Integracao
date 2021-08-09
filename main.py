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
    # lista = [{'nome':'lukas', 'idade': '', 'salario':800}]
    #
    # for i in lista:
    #
    #     if type(i['idade']) == str:
    #
    #         if i['idade'] == '':
    #
    #             numero = 0
    #             i.update({'idade': numero})
    #
    #         else:
    #             numero_ = float(i['idade'])
    #             print(numero_)
    #             i.update({'idade': numero_})
    #
    #     print(i)