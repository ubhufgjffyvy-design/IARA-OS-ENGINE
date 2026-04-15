import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
import subprocess
import sys
import threading
import time

class IaraApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Título
        self.add_widget(Label(text="Bem-vindo à IA IARA-OS-ENGINE", font_size=24, size_hint_y=None, height=50))

        # Botões
        self.add_widget(Button(text="Calculadora", on_press=self.run_calculator, size_hint_y=None, height=50))
        self.add_widget(Button(text="Terminal de Conversação", on_press=self.run_terminal, size_hint_y=None, height=50))
        self.add_widget(Button(text="Gerar Apresentação", on_press=self.run_presentation, size_hint_y=None, height=50))
        self.add_widget(Button(text="Verificar Antivírus", on_press=self.antivirus, size_hint_y=None, height=50))
        self.add_widget(Button(text="Sair", on_press=self.quit_app, size_hint_y=None, height=50))

        # Iniciar otimização automática em background
        threading.Thread(target=self.optimize_system_background, daemon=True).start()

    def run_calculator(self, instance):
        try:
            subprocess.run([sys.executable, 'calculator.py'])
        except Exception as e:
            self.show_popup("Erro", f"Erro ao executar calculadora: {e}")

    def run_terminal(self, instance):
        try:
            subprocess.run([sys.executable, 'terminal.py'])
        except Exception as e:
            self.show_popup("Erro", f"Erro ao executar terminal: {e}")

    def run_presentation(self, instance):
        try:
            subprocess.run([sys.executable, 'generate_pp.py'])
            self.show_popup("Sucesso", "Apresentação gerada: apresentacao_ia.pptx")
        except Exception as e:
            self.show_popup("Erro", f"Erro ao gerar apresentação: {e}")

    def antivirus(self, instance):
        try:
            # Assumindo que clamav está instalado
            result = subprocess.run(['clamscan', '-r', '/home'], capture_output=True, text=True, timeout=60)
            self.show_popup("Antivírus", f"Scan completo:\n{result.stdout}")
        except subprocess.TimeoutExpired:
            self.show_popup("Antivírus", "Scan demorou muito e foi cancelado.")
        except Exception as e:
            self.show_popup("Erro", f"Erro no scan antivírus: {e}. Instale clamav se necessário.")

    def optimize_system_background(self):
        while True:
            time.sleep(3600)  # Otimizar a cada hora
            self.optimize_system()

    def optimize_system(self):
        try:
            subprocess.run(['sudo', 'apt', 'clean'], check=True)
            result_disk = subprocess.run(['df', '-h'], capture_output=True, text=True, check=True)
            result_mem = subprocess.run(['free', '-h'], capture_output=True, text=True, check=True)
            # Silencioso, sem popup
        except:
            pass

    def quit_app(self, instance):
        App.get_running_app().stop()

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.8))
        popup.open()

class IaraOSApp(App):
    def build(self):
        return IaraApp()

if __name__ == '__main__':
    IaraOSApp().run()