#2. Interpolação de Lagrange

Python
def interpolacao_lagrange(x_pontos, y_pontos, x_alvo):
    n = len(x_pontos)
    resultado = 0.0
    for i in range(n):
        termo = y_pontos[i]
        for j in range(n):
            if i != j:
                termo *= (x_alvo - x_pontos[j]) / (x_pontos[i] - x_pontos[j])
        resultado += termo
    return resultado
