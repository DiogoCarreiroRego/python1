def par(numero):
    return numero % 2 != 0

if __name__ == '__main__':
    while True:
        num = int(input('Digite o número inicial: '))
        quantos = int(input('Quantos? '))

        for x in range(num, quantos + 1):
            if par(x):
                print(x)

        continuar = input('Repetir [s | n]? ')
        if continuar == 'n':
            break
    print(f'Adeus!')