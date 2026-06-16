# --- RESOLUÇÃO ALTERNATIVA INTERPOLACAO LAGRANGE E NEWTON VIA SISTEMA LINEAR (VANDERMONDE) ---

# Dados do Drone (Página 6)
t_dados = [1.0, 2.0, 3.0, 4.0, 5.0] [cite: 33]
y_dados = [1.2, 1.9, 3.2, 5.5, 8.2] [cite: 33]
t_alvo = 3.5 [cite: 34]

# 1. Construção Automatizada e Nativa da Matriz de Vandermonde
A_vandermonde = []
for x in t_dados:
    # Cada linha será: [1, x, x^2, x^3, x^4]
    linha = [x**grau for grau in range(len(t_dados))]
    A_vandermonde.append(linha)

# 2. Resolver o sistema para encontrar os coeficientes [a0, a1, a2, a3, a4]
coeficientes = eliminacao_gauss(A_vandermonde, y_dados)

# 3. Função Nativa para Avaliar o Polinômio Encontrado no ponto t_alvo
def avaliar_polinomio(coefs, x_alvo):
    resultado = 0.0
    for grau, c in enumerate(coefs):
        resultado += c * (x_alvo ** grau)
    return resultado

altitude_estimada = avaliar_polinomio(coeficientes, t_alvo)

print("--- Resolução por Sistema Linear (Vandermonde) ---")
print(f"Coeficientes encontrados (a0 até a4): {[round(c, 4) for c in coeficientes]}")
print(f"A altitude do drone em t = {t_alvo}s é: {altitude_estimada:.4f} metros")
