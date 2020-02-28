import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        image_logo = "/Users/emers/Desktop/crawler_project/pysimplegui_crawler/logo.png"
        # layout
        layout = [
            [sg.Image(image_logo)],
            [sg.Text("Usuário Synsuite"), sg.Input(size=(20, 1), key="user")],
            [sg.Text("Senha  Synsuite "), sg.Input(size=(20, 1), password_char="*", key="password")],
            [sg.Text( "Tipo de produto  "), sg.InputCombo(('Keo', 'tp-link'), size=(20, 1))],
            [sg.Text("Quantidade"), sg.Input(key="qntd", default_text="00"), sg.Text("Valor do Produto"), sg.Input(key="value", default_text="0,00")],
            [sg.Button("INICIAR")]
        ]
        # janela
        janela = sg.Window("Sistema Automatizado de patrimonios").layout(layout)
        # extrair dados da janela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)


tela = TelaPython()
tela.Iniciar()
