import PySimpleGUI as sg


#criação primeira janela
def make_window1():
    layout = [[ sg.Text("\nPalpite gerado!")],
              [ sg.Text("Qual seu chute: ",key='-OUTPUT-')],
              [sg.Input(key='chute')],
              [sg.Button('PROXIMO'), sg.Button('Fechar')]]

    return sg.Window('Jogo Da Sorte ', layout, )


#criando um loop de leitura do evento
def main():
    nome = make_window1(), None
    while True:#loop
       
        window, event, values = sg.read_all_windows()
         #serve para fechar a primeira janela caso aperte fechar
        if window == nome and event in (sg.WIN_CLOSED, 'Fechar'):
            break
        #proxima janela
        if event == 'INICIAR':
        # Atualize o elemento de texto "output" para ser o valor do elemento "input"
            window['-OUTPUT-'].update(values['chute'])#saida de valares 
    

window.main()
   
