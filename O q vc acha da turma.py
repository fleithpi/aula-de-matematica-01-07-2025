def verificar_resposta():
    while True:
        resposta = input("Você acha que a sua turma é do Carvalho? (sim/não): ").strip().lower()

        if resposta == "sim":
            print("Acertou, miserávi! 🎉")
            break
        elif resposta == "não":
            print("Resposta errada, vamos tentar novamente! ❌")
        else:
            print("Por favor, responda apenas com 'sim' ou 'não'. 🤔")

verificar_resposta()
