import PySimpleGUI as sg

class TelaPython:
    def __init__(self) -> None:
        #layout
        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Idade'), sg.Input()],
            [sg.Button(('Enviar Dados'))]
        ]
        #janela
        janela = sg.Window('Dados do Usuáro').layout(layout)
        #extrair dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)
tela = TelaPython()
tela.Iniciar()
