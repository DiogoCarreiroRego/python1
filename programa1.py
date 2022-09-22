"""
ESTE PROGRAMA IMPLEMENTA FUNÇÕES ARITMÉTRICAS
"""


def aritmetic(valor1, valor2, op='+'):
    """
    Esta função implementa as operações de somar, subtrair, multiplicar e dividir
    :param valor1:  Primeiro fator da operação
    :param valor2:  Segundo fator de operaçõa
    :param op:      Operação; valores válidos são; + - : *
    :return:        Resultado da operação
    """
    total = 'Códico de operação inválido'
    if op == '+':
        total = valor1 + valor2
    if op == '-':
        total = valor1 - valor2
    if op == ':':
        total = valor1 / valor2
    if op == '*':
        total = valor1 * valor2

    return total


if __name__ == '__main__':
    fator1 = 10
    fator2 = 20
    operacao = '-'

    print(f'{fator1} mais {fator2} = {aritmetic(fator1, fator2, operacao)}')
