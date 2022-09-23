"""
ESTE PROGRAMA IMPLEMENTA FUNÇÕES ARITMÉTRICAS
"""


def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    #return True
    #return False

"""
def par(numero):
    resto = numero % 2
    if resto == 0:
        return True
    else:
        return False
"""

"""
def par(numero):
    return numero % 2 == 0
"""

if __name__ == '__main__':
    nome = input('Como te chamas? ')
    while True:
        num = int(input('Digite o número: '))

        if par(num):
            print(f'O número {num} é par.')
        else:
            print(f'O número {num} é impar.')

        continuar = input('Repetir [s | n]? ')
        if continuar == 'n':
            break
    print(f'Adeus {nome}!')