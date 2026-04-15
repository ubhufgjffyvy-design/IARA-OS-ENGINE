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

## Tela Inicial (GUI)

Para uma interface gráfica inicial, incluímos uma tela com botões para acessar as funcionalidades.

### Como usar a Tela Inicial

Execute o script `gui.py`:

```bash
python gui.py
```

Clique nos botões para executar a calculadora, o terminal ou gerar a apresentação. A otimização do sistema ocorre automaticamente a cada hora em background (requer permissões sudo). O botão 'Verificar Antivírus' executa um scan usando clamav (instale com 'sudo apt install clamav' se necessário).

### Solução de Problemas

- Certifique-se de ter Python instalado.
- Para a apresentação, instale as dependências com pip.
- A calculadora não aceita entradas não numéricas; use números válidos.