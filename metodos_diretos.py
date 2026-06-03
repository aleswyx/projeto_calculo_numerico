def eliminacao_gauss(A, b):
    """
    Resolve o sistema linear Ax = b usando Eliminação de Gauss com pivotamento parcial.
    A: Matriz dos coeficientes (lista de listas).
    b: Vetor de constantes (lista).
    """
    n = len(b)
    
    # Construindo a matriz aumentada [A | b]
    M = []
    for i in range(n):
        linha = A[i].copy()
        linha.append(b[i])
        M.append(linha)
        
    # Etapa de Eliminação
    for i in range(n):
        # Pivotamento Parcial
        max_row = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[max_row][i]):
                max_row = k
        
        # Troca as linhas
        M[i], M[max_row] = M[max_row], M[i]
        
        # Zerando os elementos abaixo da diagonal principal
        for j in range(i + 1, n):
            if M[i][i] == 0:
                raise ValueError("O sistema não tem solução única (divisão por zero).")
                
            fator = M[j][i] / M[i][i]
            for k in range(i, n + 1):
                M[j][k] -= fator * M[i][k]
                
    # Etapa de Substituição Retroativa
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - soma) / M[i][i]
        
    return x

# === TESTE GAUSS ===
# Exemplo 2 do slide de Gauss (Página 33 do primeiro PDF)
A_teste = [[3, 2, 4], [1, 1, 2], [4, 3, -2]]
b_teste = [1, 2, 3]
solucao_gauss = eliminacao_gauss(A_teste, b_teste)
print(f"Solução Gauss: {solucao_gauss}") # Esperado aproximado: [-3.0, 5.0, 0.0]
