import PySimpleGUI as sg

class TelaPython:
    def __init__(self) -> None:
        sg.change_look_and_feel('DarkBlue') #https://user-images.githubusercontent.com/46163555/173203488-7fef44b5-000f-48b9-b353-625c214e41d4.png
        #layout
        layout = [
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(15, 0), key='idade')],
            [sg.Text('Quais os provedores de e-mail são aceitos ?')],
            [sg.Checkbox('Gmail', key='gmail')], [sg.Checkbox('Outlook', key='outlook')], [sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartões',key='aceitaCartao'), sg.Radio('Não', 'cartões', key='naoAceitaCartao')],
            [sg.Slider(range=(0, 255), default_value=0, orientation='h', size=(15, 20), key='sliderVelocidade')],
            [sg.Button(('Enviar Dados'))],
            [sg.Output(size=(30, 20))]
        ]
        #janela
        self.janela = sg.Window('Dados do Usuáro').layout(layout)

    def Iniciar(self):
        while True:
            #extrair dados da tela
            self.button, self.values = self.janela.Read()
            for key,value in self.values.items():
                print(f'{key}: {value}')