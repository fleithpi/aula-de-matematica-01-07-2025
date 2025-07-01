import numpy as np
import matplotlib.pyplot as plt

def funcao_afim(a, b, x):
    """Retorna os valores da função afim f(x) = ax + b para um array de x."""
    return a * x + b

# Solicita os coeficientes ao usuário
a = float(input("Digite o valor de 'a' (coeficiente angular): "))
b = float(input("Digite o valor de 'b' (coeficiente linear): "))

# Define o intervalo de x
x = np.linspace(-10, 10, 100)  # Gera 100 pontos entre -10 e 10
y = funcao_afim(a, b, x)

# Criando o gráfico
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f"f(x) = {a}x + {b}", color="b")
plt.axhline(0, color="black", linewidth=1)  # Linha do eixo x
plt.axvline(0, color="black", linewidth=1)  # Linha do eixo y
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.title("Gráfico da Função Afim")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()

