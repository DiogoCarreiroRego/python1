"""
ESTE PROGRAMA DÁ A "LETRA" DA NOTA
"""

def notas(nt):
    nota = 'Nota Inválida'
    if nt >= 90 <= 100:
        nota = 'A'
    elif nt >= 89 <= 70:
        print('B')
    elif nt >= 69 <= 50:
        print('C')
    elif nt >= 49 <= 30:
        print('D')
    elif nt >= 29 <= 10:
        print('E')
    elif nt >= 9 <= 0:
        print('F')

    return nota


if __name__ == '__main__':
    nota = int(input('Qual foi a sua nota? '))

    print(f'Tem um = {notas(nota)}')
"""
def notas(nt):
    nota = 'Nota Inválida'
    if nt <= 100 <=90:
        nota = 'A'
    elif nt <= 89 <= 70:
        nota = 'B'
    elif nt <= 69 <= 50:
        nota = 'C'
    elif nt <= 49 <= 30:
        nota = 'D'
    elif nt <= 29 <= 10:
        nota = 'E'
    elif nt <= 9 <= 0:
        nota = 'F'

    return nota

if __name__ == '__main__':
    nota = int(input('Qual foi a sua nota? '))

    print(f'Tem um = {notas(nota)}')
"""