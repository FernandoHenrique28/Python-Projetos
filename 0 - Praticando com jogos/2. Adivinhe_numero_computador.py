import random

# A função `guess(x)` recebe um número `x` como argumento, que representa o limite superior
# para o intervalo de números a serem adivinhados.

def guess(x):
    # Gera um número aleatório entre 1 e x (inclusive) e armazena-o na variável `random_number`.
    random_number = random.randint(1, x)

    # Inicializa a variável `guess` com 0. Essa variável vai armazenar as tentativas do jogador.
    guess = 0

    # Entra em um loop enquanto o palpite do jogador for diferente do número aleatório.
    while guess != random_number:
        # Solicita ao jogador que adivinhe um número dentro do intervalo especificado.
        guess = int(input(f'Guess a number between 1 and {x}: '))

        # Compara o palpite do jogador com o número aleatório e fornece dicas.
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
            
    print(f'Congrats! You have guessed the number {random_number}')

# Chama a função `guess(10)` com um limite superior de 10, ou seja, o jogador deve adivinhar
guess(10)
