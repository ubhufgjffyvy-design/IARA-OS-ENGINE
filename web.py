from flask import Flask, request, jsonify, render_template_string
import google.generativeai as genai
import os
import requests
from bs4 import BeautifulSoup
import webbrowser
import threading

app = Flask(__name__)

# Configure API Key from environment
api_key = os.environ.get('GOOGLE_API_KEY')
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
else:
    model = None

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>IARA-OS-ENGINE Web</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .container { max-width: 600px; margin: auto; }
            .chat { border: 1px solid #ccc; padding: 10px; height: 300px; overflow-y: scroll; }
            input { width: 80%; padding: 10px; }
            button { padding: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>IARA-OS-ENGINE Web</h1>
            <p>Configure sua API Key no terminal: export GOOGLE_API_KEY=sua_chave</p>
            <div class="chat" id="chat"></div>
            <input type="text" id="message" placeholder="Digite sua mensagem">
            <button onclick="sendMessage()">Enviar</button>
        </div>
        <script>
            async function sendMessage() {
                const message = document.getElementById('message').value;
                if (!message) return;
                document.getElementById('chat').innerHTML += '<p>Você: ' + message + '</p>';
                document.getElementById('message').value = '';
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: message })
                });
                const data = await response.json();
                document.getElementById('chat').innerHTML += '<p>IA: ' + data.reply + '</p>';
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/chat', methods=['POST'])
def chat():
    if not model:
        data = request.get_json()
        message = data.get('message', '').lower()
        if 'jogo' in message or 'game' in message:
            reply = """import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo Simples")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()"""
        else:
            reply = 'IA: Resposta simulada. Configure a API Key para respostas reais.'
        return jsonify({'reply': reply})
    data = request.get_json()
    message = data.get('message', '')
    try:
        response = model.generate_content(message)
        reply = response.text
    except Exception as e:
        reply = f'Erro: {e}'
    return jsonify({'reply': reply})

def open_browser():
    threading.Timer(1.5, lambda: webbrowser.open('http://127.0.0.1:5000')).start()

if __name__ == '__main__':
    open_browser()
    app.run(host='0.0.0.0', port=5000, debug=False)