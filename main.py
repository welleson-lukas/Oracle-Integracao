from send_to_api import *
from login_api import *


def execute_main():
    print("OLÁ, ATENÇÃO AOS PASSOS SEGUINTES!")
    input_id = int(input('INFORME O ID DA EMPRESA GERADO NO ADMIN INSIGHT: '))
    input_inicio = input('INFORME A DATA INICIAL (Exemplo: 01/01/2020): ')
    input_fim = input('INFORME A DATA FINAL (Exemplo: 01/01/2020): ')

    print(f"O ID INFORMADO É: {input_id}")
    print(f"O PERIODO INFORMADO É: {input_inicio} - {input_fim}")

    confirm_dados = input("CONFIRMAR INFORMAÇÕES? (y - SIM / n - NÃO): ")
    confirm_envio = input("INICIAR ENVIO DE DADOS? (y - SIM / n - NÃO): ")

    if confirm_dados == 'y' or confirm_dados == 'Y':
        if confirm_envio == 'y' or confirm_envio == 'Y':
            send_fornecedor()
            send_produto()
            send_historico()
            send_vendas()
            send_entrada()
            send_pedidos()
            send_estoque()

            print("INTEGRAÇÃO CONCLUIDA COM SUCESSO!")

        else:
            print("OPERAÇÃO ABORTADA!")
            return None

    else:
        print("OPERAÇÃO ABORTADA!")
        return None


if __name__ == '__main__':
    execute_main()
