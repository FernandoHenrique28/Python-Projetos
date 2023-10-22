import random

# Define a função computer_guess que recebe um número x como argumento.
def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    # Entra em um loop enquanto o feedback do usuário não for 'c' (correto).
    while feedback != 'c':
        # Gera um palpite aleatório dentro do intervalo definido por low e high.
        if low <= high:  # Verifica se ainda há um intervalo válido para adivinhar.
            guess = random.randint(low, high)
        else:
            guess = low  # Se o intervalo não é válido, o palpite deve ser low.

        # Solicita feedback do usuário (se o palpite do computador é alto, baixo ou correto).
        feedback = input(f'{guess} too high (H), too low (L), or correct (C)? ')

        # Atualiza o intervalo com base no feedback do usuário.
        if feedback == 'h':
            high = guess - 1  # Atualiza o limite superior do intervalo.
        elif feedback == 'l':
            low = guess + 1  # Atualiza o limite inferior do intervalo.

    # Quando o feedback do usuário for 'c' (correto), o loop termina, e o jogo está concluído.
    print(f'Congrats! The computer guessed your number, {guess} correctly!')

# Chama a função computer_guess com um limite superior de 100 (jogador deve adivinhar entre 1 e 100).
computer_guess(100)
