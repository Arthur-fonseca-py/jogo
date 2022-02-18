import random

def gera():
    return random.randint(1,10)
    #cria um valor aleatorio

def game():
    resposta = gera()
    tentativa = 0
    print("\nPalpite gerado!")

    chute=0
    while chute is not resposta:
        tentativa +=1#toda vez que ele tentar adiciona 1
        chute = int(input("Qual seu chute: "))
        if chute > resposta:
            print("Errou! É um valor menor que ", chute)
        elif chute < resposta:
            print("Errou! É um valor maior que ", chute)
        else:
            print("Parabéns! O número gerado foi ",resposta, \
                  "Acertou em ",tentativa," tentativas!")
    
while True:
    game()

