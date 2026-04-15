def main():
    print("Bem-vindo ao Terminal de Conversação da IA IARA-OS-ENGINE!")
    print("Digite 'sair' para encerrar a conversa.")
    print()

    while True:
        user_input = input("Você: ").strip().lower()

        if user_input == 'sair':
            print("IA: Até logo! Foi um prazer conversar.")
            break
        elif user_input in ['oi', 'olá', 'ola']:
            print("IA: Olá! Como posso ajudar hoje?")
        elif 'ajuda' in user_input:
            print("IA: Posso ajudar com programação, criação de arquivos, correção de erros e conversação natural.")
        elif 'programa' in user_input or 'aplicativo' in user_input:
            print("IA: Posso criar programas e aplicativos sem erros. Que tipo de aplicação você gostaria?")
        elif 'arquivo' in user_input:
            print("IA: Posso criar e corrigir arquivos de código, configurações e documentação.")
        else:
            print("IA: Desculpe, não entendi. Pode reformular a pergunta?")

if __name__ == "__main__":
    main()