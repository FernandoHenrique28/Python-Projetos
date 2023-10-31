from time import sleep 

# Define a função 'contador' que realiza a contagem de acordo com os parâmetros recebidos
def contador(inicio, fim, passo):
    if passo < 0:  # Se o passo for negativo, transforma em positivo
        passo *= -1
    if passo == 0:  # Se o passo for zero, define o passo como 1
        passo = 1

   
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} em {passo}')
    sleep(0.5) 

    if inicio < fim:  # Se a contagem for crescente
        cont = inicio
        while cont <= fim:  # Executa um loop enquanto 'cont' é menor ou igual a 'fim'
            print(f'{cont} ', end='', flush=True) 
            sleep(0.5)  
            cont += passo  # Atualiza o valor de 'cont' somando o passo
        print('FIM')  
    else:  # Se a contagem for decrescente
        cont = inicio
        while cont >= fim:  # Executa um loop enquanto 'cont' é maior ou igual a 'fim'
            print(f'{cont} ', end='', flush=True) 
            sleep(0.5)  
            cont -= passo  # Atualiza o valor de 'cont' subtraindo o passo
        print('FIM')  

# PROGRAMA PRINCIPAL
contador(1, 10, 1)  # Chama a função para fazer a contagem de 1 a 10, passo 1
contador(10, 0, 2)  # Chama a função para fazer a contagem de 10 a 0, passo 2
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem')
inicio = int(input('Início: '))  
fim = int(input('Fim: '))  
passo = int(input('Passo: '))  
contador(inicio, fim, passo)  # Chama a função com os valores personalizados
