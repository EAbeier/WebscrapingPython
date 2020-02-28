import PySimpleGUI as sg


# from webscrap_emerson import crawler

class TelaPython:
    def __init__(self):
        image_logo = "/Users/noc03/PycharmProjects/crawler_project/pysimplegui_crawler/logo.png"
        # layout
        layout = [
            [sg.Image(image_logo)],
            [sg.Text("Usuário Synsuite"), sg.Input(size=(20, 1), key="user")],
            [sg.Text("Senha  Synsuite "), sg.Input(size=(20, 1), password_char="*", key="password")],
            [sg.Text("Tipo de produto  "), sg.InputCombo(('Keo', 'tp-link'), key="tp_equipamento", size=(20, 1))],
            [sg.Text("Quantidade"), sg.Input(key="qntd", default_text="00"), sg.Text("Valor do Produto"),
             sg.Input(key="value", default_text="0,00")],
            [sg.Button("INICIAR")]
        ]

        # janela
        janela = sg.Window("Sistema Automatizado de patrimonios").layout(layout)
        # extrair dados da janela
        self.button, self.values = janela.Read()

    def Nserie(self):
        image_logo = image_logo = "/Users/noc03/PycharmProjects/crawler_project/pysimplegui_crawler/logo.png"
        layout = [
            [sg.Text("Número de Serie: "), sg.Input(size=(30, 1), key="nserie")],
            [sg.Button("ENVIAR")]
        ]
        # janela
        janela = sg.Window("Sistema Automatizado de patrimonios - numero de serie").layout(layout)
        # extrair dados da janela
        self.button, self.values = janela.Read()
        janela.close()
        return self.values['nserie']

    def Patrimonio(self):
        image_logo = image_logo = "/Users/noc03/PycharmProjects/crawler_project/pysimplegui_crawler/logo.png"
        layout = [
            [sg.Text("Patrimônio: "), sg.Input(size=(20, 1), key="patrimonio")],
            [sg.Button("ENVIAR")]
        ]
        # janela
        janela = sg.Window("Sistema Automatizado de patrimonios - Patrimonio").layout(layout)
        # extrair dados da janela
        self.button, self.values = janela.Read()
        janela.close()
        return self.values['patrimonio']

    def Mac(self):
        image_logo = image_logo = "/Users/noc03/PycharmProjects/crawler_project/pysimplegui_crawler/logo.png"
        layout = [
            [sg.Text("MAC: "), sg.Input(size=(20, 1), key="mac")],
            [sg.Button("ENVIAR")]
        ]
        # janela
        janela = sg.Window("Sistema Automatizado de patrimonios - MAC").layout(layout)
        # extrair dados da janela
        self.button, self.values = janela.Read()
        janela.close()
        return self.values['mac']

    def MacErrada(self):
        image_logo = image_logo = "/Users/noc03/PycharmProjects/crawler_project/pysimplegui_crawler/logo.png"
        layout = [
            [sg.Text("INSIRA MAC VALIDA ")],
            [sg.Button("OK")]
        ]
        # janela
        janela = sg.Window("Sistema Automatizado de patrimonios - MAC").layout(layout)
        # extrair dados da janela
        self.button = janela.Read()
        janela.close()



tela = TelaPython()
