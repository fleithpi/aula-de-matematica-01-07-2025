def soma_pa(a, r, n):
    """Calcula a soma dos n primeiros termos de uma progressão aritmética"""
    Sn = (n / 2) * (2 * a + (n - 1) * r)
    return Sn

# Entrada de dados
a = float(input("Digite o primeiro termo (a): "))
r = float(input("Digite a razão (r): "))
n = int(input("Digite o número de termos (n): "))

# Cálculo e saída
soma = soma_pa(a, r, n)
print(f"A soma dos {n} primeiros termos da PA é: {soma}")