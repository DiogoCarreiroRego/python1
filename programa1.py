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
    nome = input('Como te chamas ')
    while True:
        #fator1 = int(input('Digite o primeiro número: '))
        fator1 = float(input('Digite o primeiro número: '))
        #fator2 = int(input('Digite o segundo número: '))
        fator2 = float(input('Digite o segundo número: '))
        operacao = input('Qual é o operador [+, -, :, *]: ')

        print(f'Olá {nome}, {fator1} {operacao} {fator2} = {aritmetic(fator1, fator2, operacao)}')

        continuar = input('Repetir [s | n]? ')
        if continuar == 'n':
            break
    print(f'Adeus {nome}!')