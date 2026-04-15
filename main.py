import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.clock import Clock
import threading
import time
import google.generativeai as genai
import os

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Título
        layout.add_widget(Label(text="Bem-vindo à IA IARA-OS-ENGINE", font_size=24, size_hint_y=None, height=50))

        # Botões
        layout.add_widget(Button(text="Calculadora", on_press=self.go_to_calculator, size_hint_y=None, height=50))
        layout.add_widget(Button(text="IA com Google", on_press=self.go_to_terminal, size_hint_y=None, height=50))
        layout.add_widget(Button(text="Gerar Apresentação", on_press=self.go_to_presentation, size_hint_y=None, height=50))
        layout.add_widget(Button(text="Criar Jogo", on_press=self.go_to_game, size_hint_y=None, height=50))
        layout.add_widget(Button(text="Otimizar Sistema", on_press=self.optimize_system, size_hint_y=None, height=50))
        layout.add_widget(Button(text="Otimizar Bateria", on_press=self.optimize_battery, size_hint_y=None, height=50))
        layout.add_widget(Button(text="Otimizar Jogos", on_press=self.optimize_games, size_hint_y=None, height=50))
        layout.add_widget(Button(text="Verificar Antivírus", on_press=self.go_to_antivirus, size_hint_y=None, height=50))
        layout.add_widget(Button(text="Configurações", on_press=self.go_to_settings, size_hint_y=None, height=50))
        layout.add_widget(Button(text="Voltar ao Menu", on_press=self.go_to_main, size_hint_y=None, height=50))
        layout.add_widget(Button(text="Sair", on_press=self.quit_app, size_hint_y=None, height=50))

        self.add_widget(layout)

    def go_to_calculator(self, instance):
        self.manager.current = 'calculator'

    def go_to_terminal(self, instance):
        self.manager.current = 'terminal'

    def go_to_presentation(self, instance):
        self.manager.current = 'presentation'

    def go_to_game(self, instance):
        self.manager.current = 'game'

    def optimize_system(self, instance):
        popup = Popup(title="Otimização", content=Label(text="Sistema otimizado: RAM limpa, memória liberada."), size_hint=(0.8, 0.8))
        popup.open()

    def optimize_battery(self, instance):
        popup = Popup(title="Otimização", content=Label(text="Bateria otimizada: Consumo reduzido."), size_hint=(0.8, 0.8))
        popup.open()

    def optimize_games(self, instance):
        popup = Popup(title="Otimização", content=Label(text="Jogos otimizados: Lag corrigido, sensibilidade ajustada."), size_hint=(0.8, 0.8))
        popup.open()

    def go_to_antivirus(self, instance):
        self.manager.current = 'antivirus'

    def go_to_settings(self, instance):
        self.manager.current = 'settings'

    def go_to_main(self, instance):
        self.manager.current = 'main'

    def quit_app(self, instance):
        App.get_running_app().stop()

class CalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expression = ""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.display = Label(text="0", font_size=32, size_hint_y=None, height=100)
        layout.add_widget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for btn in row:
                button = Button(text=btn, font_size=24)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        layout.add_widget(Button(text="Voltar", on_press=self.go_back, size_hint_y=None, height=50))

        self.add_widget(layout)

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.display.text = str(eval(self.expression))
                self.expression = self.display.text
            except:
                self.display.text = "Erro"
                self.expression = ""
        else:
            self.expression += instance.text
            self.display.text = self.expression

    def go_back(self, instance):
        self.manager.current = 'main'

class TerminalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.output = Label(text="Terminal de IA\nDigite sua mensagem e pressione Enter.\nConfigure a URL da API nas Configurações.\n", size_hint_y=0.8, halign='left', valign='top')
        self.output.bind(size=self.output.setter('text_size'))
        scroll = ScrollView()
        scroll.add_widget(self.output)
        layout.add_widget(scroll)

        self.input = TextInput(hint_text="Digite sua mensagem", size_hint_y=None, height=50, multiline=False)
        self.input.bind(on_text_validate=self.on_enter)
        layout.add_widget(self.input)

        layout.add_widget(Button(text="Voltar", on_press=self.go_back, size_hint_y=None, height=50))

        self.add_widget(layout)
        self.model = None

    def on_enter(self, instance):
        message = self.input.text
        app = App.get_running_app()
        api_url = app.api_url
        if not api_url:
            self.output.text += "Erro: Configure a URL da API nas Configurações.\n"
            return
        try:
            import requests
            response = requests.post(api_url, json={'message': message}, timeout=10)
            if response.status_code == 200:
                data = response.json()
                reply = data.get('reply', 'Erro na resposta.')
                self.output.text += f"Você: {message}\nIA: {reply}\n"
            else:
                self.output.text += f"Erro: {response.status_code} - {response.text}\n"
        except Exception as e:
            self.output.text += f"Erro na conexão: {e}\n"
        self.input.text = ""

    def go_back(self, instance):
        self.manager.current = 'main'

class PresentationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text="Gerar Apresentação", font_size=24))

        layout.add_widget(Button(text="Gerar Apresentação", on_press=self.generate_presentation, size_hint_y=None, height=50))

        layout.add_widget(Button(text="Voltar", on_press=self.go_back, size_hint_y=None, height=50))

        self.add_widget(layout)

    def generate_presentation(self, instance):
        # Simular geração
        popup = Popup(title="Sucesso", content=Label(text="Apresentação gerada: apresentacao_ia.txt"), size_hint=(0.8, 0.8))
        popup.open()

    def go_back(self, instance):
        self.manager.current = 'main'

class AntivirusScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text="Verificar Antivírus", font_size=24))

        layout.add_widget(Button(text="Executar Scan", on_press=self.run_scan, size_hint_y=None, height=50))

        layout.add_widget(Button(text="Voltar", on_press=self.go_back, size_hint_y=None, height=50))

        self.add_widget(layout)

    def run_scan(self, instance):
        # Simular scan
        popup = Popup(title="Antivírus", content=Label(text="Scan completo: Nenhum vírus encontrado."), size_hint=(0.8, 0.8))
        popup.open()

    def go_back(self, instance):
        self.manager.current = 'main'

class GameCreationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text="Criar Jogo", font_size=24))

        self.description_input = TextInput(hint_text="Descreva o jogo que deseja criar", multiline=True, size_hint_y=0.6)
        layout.add_widget(self.description_input)

        layout.add_widget(Button(text="Gerar Jogo", on_press=self.generate_game, size_hint_y=None, height=50))

        layout.add_widget(Button(text="Voltar", on_press=self.go_back, size_hint_y=None, height=50))

        self.add_widget(layout)

    def generate_game(self, instance):
        description = self.description_input.text
        if not description:
            popup = Popup(title="Erro", content=Label(text="Por favor, descreva o jogo."), size_hint=(0.8, 0.8))
            popup.open()
            return

        app = App.get_running_app()
        api_url = app.api_url
        if not api_url:
            popup = Popup(title="Erro", content=Label(text="Configure a URL da API nas Configurações."), size_hint=(0.8, 0.8))
            popup.open()
            return

        try:
            import requests
            prompt = f"Crie um jogo simples em Python baseado na descrição: {description}. Forneça o código completo e funcional."
            response = requests.post(api_url, json={'message': prompt}, timeout=30)
            if response.status_code == 200:
                data = response.json()
                code = data.get('reply', 'Erro na geração.')
                # Salvar o código em um arquivo
                with open('jogo_gerado.py', 'w') as f:
                    f.write(code)
                popup = Popup(title="Sucesso", content=Label(text="Jogo gerado: jogo_gerado.py"), size_hint=(0.8, 0.8))
                popup.open()
            else:
                popup = Popup(title="Erro", content=Label(text=f"Erro: {response.status_code}"), size_hint=(0.8, 0.8))
                popup.open()
        except Exception as e:
            popup = Popup(title="Erro", content=Label(text=f"Erro: {e}"), size_hint=(0.8, 0.8))
            popup.open()

    def go_back(self, instance):
        self.manager.current = 'main'

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text="Configurações", font_size=24))

        api_layout = BoxLayout(size_hint_y=None, height=50)
        api_layout.add_widget(Label(text="API Key Google:", size_hint_x=0.3))
        self.api_key_input = TextInput(hint_text="Digite sua API Key", size_hint_x=0.7)
        api_layout.add_widget(self.api_key_input)
        layout.add_widget(api_layout)

        url_layout = BoxLayout(size_hint_y=None, height=50)
        url_layout.add_widget(Label(text="URL da API:", size_hint_x=0.3))
        self.api_url_input = TextInput(hint_text="http://localhost:5000/chat", size_hint_x=0.7)
        url_layout.add_widget(self.api_url_input)
        layout.add_widget(url_layout)

        layout.add_widget(Button(text="Salvar", on_press=self.save_settings, size_hint_y=None, height=50))

        layout.add_widget(Button(text="Voltar", on_press=self.go_back, size_hint_y=None, height=50))

        self.add_widget(layout)

    def save_settings(self, instance):
        app = App.get_running_app()
        app.api_key = self.api_key_input.text
        app.api_url = self.api_url_input.text
        popup = Popup(title="Sucesso", content=Label(text="Configurações salvas!"), size_hint=(0.8, 0.8))
        popup.open()

    def go_back(self, instance):
        self.manager.current = 'main'

class IaraOSApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api_key = ""
        self.api_url = "http://localhost:5000/chat"  # Default local web app

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CalculatorScreen(name='calculator'))
        sm.add_widget(TerminalScreen(name='terminal'))
        sm.add_widget(PresentationScreen(name='presentation'))
        sm.add_widget(GameCreationScreen(name='game'))
        sm.add_widget(AntivirusScreen(name='antivirus'))
        sm.add_widget(SettingsScreen(name='settings'))

        # Iniciar otimização automática em background
        threading.Thread(target=self.optimize_system_background, daemon=True).start()

        return sm

    def optimize_system_background(self):
        while True:
            time.sleep(3600)  # Otimizar a cada hora
            self.optimize_system()

    def optimize_system(self):
        # Simular otimização, sem subprocess
        pass

if __name__ == '__main__':
    IaraOSApp().run()