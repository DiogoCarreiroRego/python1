def par(numero):
    return numero % 2 != 0

if __name__ == '__main__':
    while True:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        primos = 0

        for x in range(num1, num2 + 1):
            if par(x):
                primos += 1
                print(x)
        print(f'Tem {primos}')

        continuar = input('Repetir [s | n]? ')
        if continuar == 'n':
            break
    print(f'Adeus!')