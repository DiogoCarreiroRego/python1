"""
ESTE PROGRAMA DÁ A "LETRA" DA NOTA
"""


def notas(nt):
    nota = 'Nota Inválida'
    if nt >=80 <=100:
        nota = 'A'
    elif nt >= 60 <= 79:
        nota = 'B'
    elif nt >= 40 <= 59:
        nota = 'C'
    elif nt >= 20 <= 39:
        nota = 'D'
    elif nt >=0 <=19:
        nota = 'E'

    return nota

if __name__ == '__main__':
    nome = input('Como te chamas? ')
    while True:
        nota = int(input('Qual foi a sua nota? '))

        print(f'{nome}, Tens um {notas(nota)}')
        continuar = input('Deseja continuar [s | n]? ')
        if continuar == 'n':
            break
    print(f'Adeus {nome}.')