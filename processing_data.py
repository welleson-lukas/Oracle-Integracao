from query_db import *
import pandas as pd
import datetime


# FORNECEDORES
def tratando_fornecedor():
    fornecedor_df = query_fornecedor()
    fornecedor_df.columns = ["cod_fornecedor", "desc_fornecedor", "cnpj", "iestadual"]

    # TODO EMPRESA
    fornecedor_df['empresa'] = 3

    fornecedor = fornecedor_df.assign(**fornecedor_df.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return fornecedor


# PRODUTOS
def tratando_produto():
    df_produtos = query_produto()
    df_produtos.columns = ["cod_fornecedor", "cod_produto", "desc_produto", "cod_ncm", "cod_auxiliar", "marca", "embalagem", "quantidade_un_cx",  "peso_liquido", "cod_fabrica", "cod_depto", "desc_departamento", "cod_sec", "desc_secao", "principio_ativo"]

    # TODO EMPRESA
    df_produtos['empresa'] = 3

    produtos_dic = df_produtos.assign(**df_produtos.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
        "records")

    return produtos_dic


# HISTORICO
def tratando_historico():
    hist_estoque_df = query_historico()
    hist_estoque_df.columns = ["cod_produto", "data", "qt_estoque", "cod_filial", "cod_fornecedor"]
    hist_estoque_df['data'] = pd.to_datetime(hist_estoque_df['data'])

    historico_df = hist_estoque_df

    # TODO EMPRESA
    historico_df['empresa'] = 3

    historico = historico_df.assign(**historico_df.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
        "records")

    return historico


# VENDAS
def tratando_venda():
    vendas_df = query_venda()
    vendas_df.columns = ["data", "cod_produto", "qt_venda", "preco_unit", "cod_filial", "cliente", "num_nota", "rca","cod_fornecedor", "custo_fin", "supervisor"]
    vendas_df['data'] = pd.to_datetime(vendas_df['data'])

    # TODO EMPRESA
    vendas_df['empresa'] = 3

    vendas_dic = vendas_df.assign(**vendas_df.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return vendas_dic


# ENTRADAS
def tratando_entrada():
    ultima_entrada_df = query_entrada()
    ultima_entrada_df.columns = ["cod_filial", "data", "vl_ult_entrada", "qt_ult_entrada", "cod_produto","cod_fornecedor"]
    ultima_entrada_df['data'] = pd.to_datetime(ultima_entrada_df['data'])

    # TODO EMPRESA
    ultima_entrada_df['empresa'] = 3

    entradas = ultima_entrada_df.assign(**ultima_entrada_df.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
        "records")

    return entradas


# PEDIDOS
def tratando_pedidos():
    df_pedidos_compras = query_pedido()
    df_pedidos_compras.columns = ["cod_filial", "cod_produto", "saldo", "num_pedido", "data", "cod_fornecedor"]
    df_pedidos_compras['data'] = pd.to_datetime(df_pedidos_compras['data'])

    pedidos_df = df_pedidos_compras

    # TODO EMPRESA
    pedidos_df['empresa'] = 3

    p_compras = pedidos_df.assign(**pedidos_df.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return p_compras


# ESTOQUE ATUAL
def tratando_estoque():
    estoque_atual_df = query_estoque()

    estoque_atual_df.columns = ["cod_filial", "cod_produto", "qt_geral", "qt_indenizada", "qt_reservada", "qt_pendente", "qt_bloqueada", "qt_disponivel", "custo_ult_entrada", "cod_fornecedor", "preco_venda"]
    estoque_atual_df['data'] = datetime.date.today()
    estoque_atual_df['data'] = pd.to_datetime(estoque_atual_df['data'])

    #TODO EMPRESA
    estoque_atual_df['empresa'] = 3

    estoque_atual = estoque_atual_df.assign(**estoque_atual_df.select_dtypes(["datetime"]).astype(str).to_dict("list")
                                            ).to_dict("records")

    return estoque_atual
