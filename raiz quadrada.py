def raiz_quadrada_newton(x, precisao=1e-6):
    """Calcula a raiz quadrada de x usando o método de Newton."""
    if x < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    
    y = x  # Chute inicial
    while abs(y * y - x) > precisao:  # Verifica a precisão
        y = (y + x / y) / 2  # Fórmula do método de Newton
    return y

# Entrada do usuário
num = float(input("Digite um número para calcular a raiz quadrada: "))

# Cálculo e saída
try:
    raiz = raiz_quadrada_newton(num)
    print(f"A raiz quadrada de {num} é aproximadamente {raiz:.6f}")
except ValueError as e:
    print(e)