def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1  # zeros = zeros + 1
    return zeros

def primo(num):
    return num % 2 != 0

if __name__ == '__main__':
    while True:
        numero = int(input('Digite o primeiro número: '))

        if primo(numero):
            print(f'O número {numero} tem {divisores(numero)} divisores e é primo.')
        else:
            print(f'O número {numero} tem {divisores(numero)} divisores e não é primo.')
        #print(f'O número {numero} tem {divisores(numero)} divisores.')

        continuar = input('Repetir [s | n]? ')
        if continuar == 'n':
            break