# IARA-OS-ENGINE

Este repositório contém uma apresentação PowerPoint sobre a IA IARA-OS-ENGINE, que cria aplicativos e arquivos sem erros, além de corrigir arquivos existentes.

## Download

A aplicação está pronta para download. Baixe o arquivo `IARA-OS-ENGINE.zip` e extraia. Instale as dependências com `pip install -r requirements.txt` e execute `python gui.py` para iniciar a interface gráfica.

## Apresentação

Execute o script `generate_pp.py` para gerar a apresentação `apresentacao_ia.pptx`.

Requisitos: Python 3 e as dependências em `requirements.txt`.

```bash
pip install -r requirements.txt
python generate_pp.py
```

## Exemplo de Programa

Como exemplo de um aplicativo criado pela IA, incluímos uma calculadora simples em Python.

### Como usar a Calculadora

Execute o script `calculator.py`:

```bash
python calculator.py
```

Siga as instruções no terminal para realizar operações matemáticas básicas.

## Terminal de Conversação

Para demonstrar as capacidades de conversação da IA, incluímos um terminal simples de comandos.

### Como usar o Terminal

Execute o script `terminal.py`:

```bash
python terminal.py
```

Interaja digitando mensagens. Digite 'sair' para encerrar.

## Versão Mobile (APK)

A aplicação foi adaptada para mobile usando Kivy. Para gerar o APK Android:

1. Instale as dependências: `pip install kivy buildozer cython`
2. Execute `buildozer android debug` (requer Android SDK, pode levar tempo)
3. O APK será gerado em `bin/`

Nota: O build do APK requer ambiente adequado com Android SDK. Em caso de problemas, consulte a documentação do Buildozer.

## Download

- Certifique-se de ter Python instalado.
- Para a apresentação, instale as dependências com pip.
- A calculadora não aceita entradas não numéricas; use números válidos.