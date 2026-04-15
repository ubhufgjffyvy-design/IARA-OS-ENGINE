import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import threading
import time

def run_calculator():
    subprocess.run([sys.executable, 'calculator.py'])

def run_terminal():
    subprocess.run([sys.executable, 'terminal.py'])

def run_presentation():
    try:
        subprocess.run([sys.executable, 'generate_pp.py'])
        messagebox.showinfo("Sucesso", "Apresentação gerada: apresentacao_ia.pptx")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar apresentação: {e}")

def optimize_system():
    try:
        subprocess.run(['sudo', 'apt', 'clean'], check=True)
        result_disk = subprocess.run(['df', '-h'], capture_output=True, text=True, check=True)
        result_mem = subprocess.run(['free', '-h'], capture_output=True, text=True, check=True)
        return f"Sistema otimizado.\n\nUso do Disco:\n{result_disk.stdout}\nUso da Memória:\n{result_mem.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar comando: {e}"
    except Exception as e:
        return f"Erro na otimização: {e}"

def optimize_system_background():
    while True:
        time.sleep(3600)  # Otimizar a cada hora
        optimize_system()  # Silencioso, sem popup

def antivirus():
    try:
        # Assumindo que clamav está instalado; caso contrário, instalar com sudo apt install clamav
        result = subprocess.run(['clamscan', '-r', '/home/codespace'], capture_output=True, text=True, timeout=60)
        messagebox.showinfo("Antivírus", f"Scan completo:\n{result.stdout}")
    except subprocess.TimeoutExpired:
        messagebox.showwarning("Antivírus", "Scan demorou muito e foi cancelado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro no scan antivírus: {e}. Instale clamav com 'sudo apt install clamav' se necessário.")

def main():
    # Iniciar otimização automática em background
    threading.Thread(target=optimize_system_background, daemon=True).start()

    root = tk.Tk()
    root.title("IARA-OS-ENGINE - Tela Inicial")
    root.geometry("400x300")

    tk.Label(root, text="Bem-vindo à IA IARA-OS-ENGINE", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Calculadora", command=run_calculator, width=20).pack(pady=10)
    tk.Button(root, text="Terminal de Conversação", command=run_terminal, width=20).pack(pady=10)
    tk.Button(root, text="Gerar Apresentação", command=run_presentation, width=20).pack(pady=10)
    tk.Button(root, text="Verificar Antivírus", command=antivirus, width=20).pack(pady=10)

    tk.Button(root, text="Sair", command=root.quit, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()