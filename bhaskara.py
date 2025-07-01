import math

def resolver_equacao_segundo_grau(a, b, c):
    """Resolve uma equação do segundo grau ax² + bx + c = 0"""
    delta = b**2 - 4*a*c  # Cálculo do discriminante (Δ)
    
    if delta > 0:
        # Duas raízes reais
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)
    elif delta == 0:
        # Uma raiz real (raízes iguais)
        x = -b / (2 * a)
        return (x,)
    else:
        # Nenhuma raiz real
        return None

# Entrada dos coeficientes a, b e c
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Verifica se é uma equação de segundo grau válida (a não pode ser zero)
if a == 0:
    print("O valor de a não pode ser zero para uma equação do segundo grau.")
else:
    # Resolve a equação e exibe os resultados
    resultado = resolver_equacao_segundo_grau(a, b, c)
    if resultado is None:
        print("A equação não possui raízes reais.")
    elif len(resultado) == 1:
        print(f"A equação tem uma raiz real: x = {resultado[0]:.2f}")
    else:
        print(f"A equação tem duas raízes reais: x1 = {resultado[0]:.2f} e x2 = {resultado[1]:.2f}")
