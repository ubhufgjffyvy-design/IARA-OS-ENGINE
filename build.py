import subprocess
import sys

def main():
    print("Construindo o executável da IA IARA-OS-ENGINE...")
    try:
        # Construir o executável com PyInstaller
        subprocess.run([
            'pyinstaller',
            '--onefile',  # Executável único
            '--windowed',  # Sem console (para GUI)
            '--name=IARA-OS-ENGINE',
            'gui.py'
        ], check=True)
        print("Executável criado em dist/IARA-OS-ENGINE")
        print("Pronto para baixar ou distribuir.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao construir: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()