def calcular_raiz_função_afim(a, b):
    """Calcula a raiz de uma função afim ax + b = 0"""
    if a == 0:
        raise ValueError("Não é possível calcular a raiz, pois 'a' não pode ser zero.")
    return -b / a

# Entrada dos coeficientes a e b
a = float(input("Digite o valor de a (coeficiente de x): "))
b = float(input("Digite o valor de b (coeficiente constante): "))

# Cálculo e saída
try:
    raiz = calcular_raiz_função_afim(a, b)
    print(f"A raiz da função afim {a}x + {b} = 0 é: x = {raiz:.2f}")
except ValueError as e:
    print(e)