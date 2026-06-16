# Interpolação de Gregory-Newton (Para pontos equidistantes)

def fatorial(n):
    res = 1
    for i in range(2, n + 1): 
        res *= i
    return res

def interpolacao_gregory_newton(x_pontos, y_pontos, x_alvo):
    n = len(x_pontos)
    h = x_pontos[1] - x_pontos[0]
    tabela = [[0.0] * n for _ in range(n)]
    
    # Preenche a primeira coluna com os valores de y
    for i in range(n): 
        tabela[i][0] = y_pontos[i]
    
    # Calcula a tabela de diferenças finitas avançadas
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = tabela[i+1][j-1] - tabela[i][j-1]
            
    resultado = y_pontos[0]
    produto = 1.0
    
    # Avaliação do polinômio interpolador
    for i in range(1, n):
        produto *= (x_alvo - x_pontos[i-1])
        resultado += (tabela[0][i] / (fatorial(i) * (h**i))) * produto
        
    return resultado


# --- BLOCO DE EXECUÇÃO EXIGIDO PELO PROFESSOR ---
if __name__ == "__main__":
    # Dados extraídos do slide 7 (Resfriamento do servidor no Data Center)
    # x (minutos): [10, 20, 30, 40]; constante h = 10
    # y (temperatura ºC): [45.0, 52.0, 60.0, 71.0]
    x_minutos = [10, 20, 30, 40]
    y_temperatura = [45.0, 52.0, 60.0, 71.0]
    x_estimar = 25

    # Execução do algoritmo nativo
    temperatura_estimada = interpolacao_gregory_newton(x_minutos, y_temperatura, x_estimar)

    # --- RETORNO DA RESPOSTA DO ALGORITMO ---
    print("=" * 50)
    print("      RESULTADO DA INTERPOLAÇÃO DE GREGORY-NEWTON     ")
    print("=" * 50)
    print(f"Dados de Tempo (x):       {x_minutos} minutos")
    print(f"Dados de Temperatura (y): {y_temperatura} ºC")
    print("-" * 50)
    print(f"Temperatura estimada no minuto {x_estimar}: {temperatura_estimada:.4f} ºC")
    print("=" * 50)
