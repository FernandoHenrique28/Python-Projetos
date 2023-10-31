from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for _ in range(5):
        numero_sorteado = randint(1, 10)
        lista.append(numero_sorteado)
        print(f'{numero_sorteado} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO')

def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da lista {lista}, temos {soma}')

numeros = []
sorteia(numeros)
soma_par(numeros)

