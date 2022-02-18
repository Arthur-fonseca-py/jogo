import PySimpleGUI as sg
#criar janelas
def tela_inicial():


    layout = [[sg.Text("\nQual seu nome!"), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Input(key='nome')],
            [sg.Button('ok'), sg.Button('fechar')]]


    window = sg.Window('Jogo Da Sorte ', layout ,["nome"].get())
 

def tela_jogo():
    sg.theme('BluePurple')

    layout = [[sg.Text("\nPalpite gerado!"), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Input(key='chute')],
            [sg.Button('ok'), sg.Button('fechar')]]

    return sg.Window ('Jogo Da Sorte ', layout,finalize=True)

#criar as janelas iniciais
janela1,janela2=tela_inicial(),None

#criar um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
        #quando a janela for fechada
    if event == sg.WIN_CLOSED and window == janela1:
            break
        #queremos ir para proxima janela
    if window == janela1 and event == "ok":
        janela2 = tela_jogo() 
        janela1.hide()

