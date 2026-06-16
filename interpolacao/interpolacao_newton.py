# Interpolação Polinomial de Newton (Diferenças Divididas)

def diferencas_divididas(x_pontos, y_pontos):
    """
    Constrói a tabela de diferenças divididas de Newton.
    """
    n = len(x_pontos)
    # Cria uma matriz n x n preenchida com zeros
    tabela = [[0.0] * n for _ in range(n)]
    
    # A primeira coluna é preenchida com os valores de y
    for i in range(n):
        tabela[i][0] = y_pontos[i]
        
    # Calcula as colunas subsequentes da tabela
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i + 1][j - 1] - tabela[i][j - 1]) / (x_pontos[i + j] - x_pontos[i])
            
    # Retorna a primeira linha da tabela, que contém os coeficientes do polinômio (a0, a1, a2...)
    return tabela[0]


def interpolacao_newton(x_pontos, y_pontos, x_alvo):
    """
    Calcula o valor interpolado no ponto x_alvo usando o Polinômio de Newton.
    """
    coeficientes = diferencas_divididas(x_pontos, y_pontos)
    n = len(coeficientes)
    
    resultado = coeficientes[0]
    produtorio = 1.0
    
    for i in range(1, n):
        produtorio *= (x_alvo - x_pontos[i - 1])
        resultado += coeficientes[i] * produtorio
        
    return resultado


# --- BLOCO DE EXECUÇÃO EXIGIDO PELO PROFESSOR ---
if __name__ == "__main__":
    # Dados extraídos do slide 6 (Telemetria do drone autônomo)
    t_dados = [1.0, 2.0, 3.0, 4.0, 5.0]
    y_dados = [1.2, 1.9, 3.2, 5.5, 8.2]
    t_alvo = 3.5
    
    # Execução do algoritmo nativo
    altitude_estimada = interpolacao_newton(t_dados, y_dados, t_alvo)
    coefs = diferencas_divididas(t_dados, y_dados)
    
    # --- RETORNO DA RESPOSTA DO ALGORITMO ---
    print("=" * 50)
    print("         RESULTADO DA INTERPOLAÇÃO DE NEWTON        ")
    print("=" * 50)
    print(f"Dados de Tempo (t):    {t_dados} s")
    print(f"Dados de Altitude (y): {y_dados} m")
    print(f"Coeficientes (a0...an): {[round(c, 4) for c in coefs]}")
    print("-" * 50)
    print(f"Altitude estimada no instante t={t_alvo}s: {altitude_estimada:.4f} metros")
    print("=" * 50)
