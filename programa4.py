"""
Imprimir os números pares entres 1 e o número inserido
"""

from programa3 import par

# range(start, stop, step)
# (step) salta números, como 2, 4, 6...
if __name__ == '__main__':
    num1 = int(input('Digite o primeiro número: '))

    for x in range(1, num1 + 1):
        if par(x):
            print(x)