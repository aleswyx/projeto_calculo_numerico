4. Gregory-Newton (Para pontos equidistantes)

Python
def fatorial(n):
    res = 1
    for i in range(2, n + 1): res *= i
    return res

def interpolacao_gregory_newton(x_pontos, y_pontos, x_alvo):
    n = len(x_pontos)
    h = x_pontos[1] - x_pontos[0]
    tabela = [[0.0] * n for _ in range(n)]
    for i in range(n): tabela[i][0] = y_pontos[i]
    
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = tabela[i+1][j-1] - tabela[i][j-1]
            
    resultado = y_pontos[0]
    produto = 1.0
    for i in range(1, n):
        produto *= (x_alvo - x_pontos[i-1])
        resultado += (tabela[0][i] / (fatorial(i) * (h**i))) * produto
    return resultado
