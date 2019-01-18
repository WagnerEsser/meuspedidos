# coding:utf-8


def remover_zeros_final(valor):  # EX: 12345.00
    return int(str(valor)[:-3])


def remover_ponto_decimal(valor):  # EX: 123.45
    valor = str(valor).split(".")
    valor = ''.join(valor)
    return int(valor)


def verificar_rentabilidade(preco_produto, preco_pago):
    if preco_pago > preco_produto:
        # ótima
        return 2
    elif preco_produto * 0.9 <= preco_pago <= preco_produto:
        # boa
        return 1
    else:
        # ruim
        return 0
