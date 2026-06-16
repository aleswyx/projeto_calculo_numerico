# --- RESOLUÇÃO ALTERNATIVA INTERPOLACAO VIA SISTEMA LINEAR (VANDERMONDE) ---

def eliminacao_gauss(A, b):
    """
    Resolve um sistema linear Ax = b de forma puramente nativa
    usando o método de Eliminação de Gauss com substituição retroativa.
    """
    n = len(b)
    
    # Criar a matriz aumentada para não modificar as listas originais
    M = [A[i][:] + [b[i]] for i in range(n)]
    
    # Passo 1: Eliminação (Triangularização)
    for i in range(n):
        # Pivoteamento parcial simples para evitar divisão por zero
        if M[i][i] == 0.0:
            for k in range(i + 1, n):
                if M[k][i] != 0.0:
                    M[i], M[k] = M[k], M[i]
                    break
            else:
                raise ValueError("O sistema linear não possui solução única.")
                
        # Zerar os elementos abaixo do pivô
        for k in range(i + 1, n):
            fator = M[k][i] / M[i][i]
            for j in range(i, n + 1):
                M[k][j] -= fator * M[i][j]
                
    # Passo 2: Substituição Retroativa
    x_solucao = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = 0.0
        for j in range(i + 1, n):
            soma += M[i][j] * x_solucao[j]
        x_solucao[i] = (M[i][n] - soma) / M[i][i]
        
    return x_solucao


def avaliar_polinomio(coefs, x_alvo):
    """
    Função Nativa para Avaliar o Polinômio Encontrado no ponto x_alvo.
    P(x) = a0 + a1*x + a2*x^2 + ...
    """
    resultado = 0.0
    for grau, c in enumerate(coefs):
        resultado += c * (x_alvo ** grau)
    return resultado


# --- BLOCO DE EXECUÇÃO EXIGIDO PELO PROFESSOR ---
if __name__ == "__main__":
    # Dados do Drone (Slide 6)
    t_dados = [1.0, 2.0, 3.0, 4.0, 5.0]
    y_dados = [1.2, 1.9, 3.2, 5.5, 8.2]
    t_alvo = 3.5

    # 1. Construção Automatizada e Nativa da Matriz de Vandermonde
    A_vandermonde = []
    for x in t_dados:
        # Cada linha será: [1, x, x^2, x^3, x^4]
        linha = [x**grau for grau in range(len(t_dados))]
        A_vandermonde.append(linha)

    # 2. Resolver o sistema para encontrar os coeficientes [a0, a1, a2, a3, a4]
    coeficientes = eliminacao_gauss(A_vandermonde, y_dados)

    # 3. Avaliar o polinômio encontrado no ponto t_alvo
    altitude_estimada = avaliar_polinomio(coeficientes, t_alvo)

    # --- RETORNO DA RESPOSTA DO ALGORITMO ---
    print("=" * 60)
    print("   INTERPOLAÇÃO VIA SISTEMA LINEAR (MATRIZ DE VANDERMONDE)   ")
    print("=" * 60)
    print(f"Coeficientes encontrados (a0 até a4): {[round(c, 4) for c in coeficientes]}")
    print("-" * 60)
    print(f"A altitude estimada do drone em t = {t_alvo}s é: {altitude_estimada:.4f} metros")
    print("=" * 60)
