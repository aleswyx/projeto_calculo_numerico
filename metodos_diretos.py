def eliminacao_gauss(A, b):
   
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

def enctrar_a0(a):
    i = len(a)
    y = 0
    for b in range(i -1):
        k = b % 2
        if k == 0:
            y += (-1) * (a[b] * 2)
        else:
            y += a[b] * 2
    l = y + 1.9
    return l

def valor_da_altura(a , c):
    i = len(a)
    k = 0
    for b in range(i):
        k += a[b] * 3.5
    y = (k + c) * (-1)
    return y

A_teste = [
    [1, 1, 1, 1, 1],
    [2, 4, 8, 16, 32],
    [3, 9, 27, 81, 243],
    [4, 16, 64, 256, 1024],
    [5, 25, 125, 625, 3125]
]

b_teste = [1.2, 1.9, 3.2, 5.5, 8.2]

solucao_gauss = eliminacao_gauss(A_teste, b_teste)
constante = enctrar_a0(solucao_gauss)
print(f"Solução Gauss: {solucao_gauss}")
altura = valor_da_altura(solucao_gauss,constante)
print(f"A altitude do drone :{altura} u.a")
