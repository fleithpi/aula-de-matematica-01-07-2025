def resolver_sistema_2x2(a1, b1, c1, a2, b2, c2):
    # Determinantes
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    if D == 0:
        if Dx == 0 and Dy == 0:
            return "Sistema indeterminado (infinitas soluções)"
        else:
            return "Sistema impossível (sem solução)"

    x = Dx / D
    y = Dy / D
    return x, y

def main():
    print("Sistema da forma:")
    print("a1*x + b1*y = c1")
    print("a2*x + b2*y = c2")

    a1 = float(input("Digite a1: "))
    b1 = float(input("Digite b1: "))
    c1 = float(input("Digite c1: "))
    a2 = float(input("Digite a2: "))
    b2 = float(input("Digite b2: "))
    c2 = float(input("Digite c2: "))

    resultado = resolver_sistema_2x2(a1, b1, c1, a2, b2, c2)

    print("\nResultado:")
    if isinstance(resultado, tuple):
        print(f"x = {resultado[0]:.4f}")
        print(f"y = {resultado[1]:.4f}")
    else:
        print(resultado)

if __name__ == "__main__":
    main()
    