import random

import PySimpleGUI as sg
#criar janelas

def tela_inicial():
    layout = [[sg.Text("\nQual seu nome!"), sg.Text(size=(15, 1), key='-OUTPUT-')],
    [sg.Input(key='nome')],
    [sg.Button('ok'), sg.Button('fechar')]]
    window = sg.Window('Jogo Da Sorte ', layout)
    event, values = window.read()
    return values['nome']

def tela_jogo(nome, acertou, resposta, tentativa):
    sg.theme('BluePurple')
    layout = [
    [sg.Text("\nOlá, " + nome), sg.Text(size=(15, 1))],
    [sg.Text("\nPalpite gerado!"), sg.Text(size=(15, 1))],
    [sg.Input(key='chute')],
    [sg.Button('ok'), sg.Button('fechar')]
    ]
    window = sg.Window('Jogo Da Sorte ', layout)

# criar um loop de leitura de eventos
while True:
    event, values = window.read()
    # Pega o valor do input de key=chute e transforma em número pq ela vem como string
    chute = int(values['chute'])
    # chama a função game e passa as variáveis para ela, o retorno dela preciso pegar 2 variáveis: resposta e tentativa
    acertou, tentativa = game(chute, acertou, resposta, tentativa)
    # Enquanto a resposta for False vai pedindo o próximo palpite
    if event == sg.WIN_CLOSED or acertou:
        break

def gera():
    return random.randint(1, 10)
# cria um valor aleatorio

def game(chute, acertou, resposta, tentativa):
    tentativa += 1 # toda vez que ele tentar adiciona 1
    if chute > resposta:
        print("Errou! É um valor menor que ", chute)
    elif chute < resposta:
        print("Errou! É um valor maior que ", chute)
    else:
        print("Parabéns! O número gerado foi ", resposta, "Acertou na", tentativa, "tentativas!")
        # Acertando o palpite é mudado acertou para True e retorna esse valor
        acertou = True
    return acertou, tentativa
            
        
if 'main' == name:
            # Retorna o nome escolhido para ser usado na próx. tela
    nome = tela_inicial()
                    # Inicializa algumas variáveis
    tentativa = 0
    acertou = False
                    # Gera um número aleatório só uma vez
    esposta = gera()
                    # Inicializa o jogo

tela_jogo(nome, acertou, resposta, tentativa)
