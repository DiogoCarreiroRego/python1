"""
ESTE PROGRAMA IMPLEMENTA FUNÇÕES ARITMÉTRICAS
"""


def par(numero):
    if num % 2 == 0:
        return True
    else:
        return False

    #return True
    #return False


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