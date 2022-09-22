"""
ESTE PROGRAMA DÁ A "LETRA" DA NOTA
"""


def notas(nt):
    nota = 'Nota Inválida'
    if nt <= 100 <=90:
        nota = 'A'
    if nt <= 89 <= 70:
        nota = 'B'
    if nt <= 69 <= 50:
        nota = 'C'
    if nt <= 49 <= 30:
        nota = 'D'
    if nt <= 29 <= 10:
        nota = 'E'
    if nt <= 9 <= 0:
        nota = 'F'

    return nota

if __name__ == '__main__':
    nota = int(input('Qual foi a sua nota? '))

    print(f'Tem um = {notas(nota)}')