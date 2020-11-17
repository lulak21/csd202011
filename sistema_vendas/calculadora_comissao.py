LIMITE_FAIXA_1 = 10000


def calcular(valor_venda):
    if valor_venda > LIMITE_FAIXA_1:
        return valor_venda * 6 / 100
    else:
        return valor_venda * 5 / 100
