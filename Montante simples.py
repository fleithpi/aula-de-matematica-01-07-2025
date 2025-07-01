def calcular_juros_compostos(principal, taxa_mensal, meses):
    """
    Calcula o montante final de um investimento com juros compostos mensais.

    :param principal: Capital inicial investido
    :param taxa_mensal: Taxa de juros mensal (em percentual)
    :param meses: Tempo do investimento (em meses)
    :return: Montante final após o período
    """
    taxa_decimal = taxa_mensal / 100  # Converte taxa percentual para decimal
    montante = principal * (1 + taxa_decimal) ** meses
    return montante

# Solicita os dados do usuário
principal = float(input("Digite o valor do investimento inicial: "))
taxa_mensal = float(input("Digite a taxa de juros mensal (%): "))
meses = int(input("Digite o período do investimento (meses): "))

# Calcula e exibe o montante final
montante_final = calcular_juros_compostos(principal, taxa_mensal, meses)
print(f"O montante final após {meses} meses será de R$ {montante_final:.2f}")