def soma_pg(a, r, n):
    """Calcula a soma dos n primeiros termos de uma progressão geométrica"""
    if r == 1:
        return n * a  # Caso especial onde a PG é constante
    return a * (1 - r**n) / (1 - r)

# Entrada de dados
a = float(input("Digite o primeiro termo (a): "))
r = float(input("Digite a razão (r): "))
n = int(input("Digite o número de termos (n): "))

# Cálculo e saída
soma = soma_pg(a, r, n)
print(f"A soma dos {n} primeiros termos da PG é: {soma}")