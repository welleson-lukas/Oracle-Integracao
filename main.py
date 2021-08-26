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

            id = input_id
            inicio = input_inicio
            fim = input_fim

            send_fornecedor(id)
            send_produto(id)
            send_historico(id, inicio, fim)
            send_vendas(id, inicio, fim)
            send_entrada(id, inicio, fim)
            send_pedidos(id, inicio, fim)
            send_estoque(id)

            print("INTEGRAÇÃO CONCLUIDA COM SUCESSO!")

        else:
            print("OPERAÇÃO ABORTADA!")
            return None

    else:
        print("OPERAÇÃO ABORTADA!")
        return None


if __name__ == '__main__':
    execute_main()
