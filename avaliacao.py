def avaliar_professor():
    while True:
        try:
            nota = int(input("Qual nota você dá ao professor Diego Castro? (0-10): "))

            if nota == 10:
                print("Obrigado pela pesquisa! 😃")
                break
            else:
                print("Resposta incorreta! Vou te dar mais uma chance... ou você quer reprovar?! 😠")
        except ValueError:
            print("Por favor, digite um número inteiro entre 0 e 10.")

avaliar_professor()
