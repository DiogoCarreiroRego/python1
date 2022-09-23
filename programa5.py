def divisores(num):


    return 1


if __name__ == '__main__':
    while True:
        numero = int(input('Digite o primeiro número: '))

        print(f'O número {numero} tem divisores {divisores(numero)}')

        continuar = input('Repetir [s | n]? ')
        if continuar == 'n':
            break