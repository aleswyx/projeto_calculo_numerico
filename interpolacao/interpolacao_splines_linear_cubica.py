# Interpolação por Splines (Linear e Cúbica Natural)

def spline_linear(t, y, valor_alvo):
    """
    Calcula a Spline Linear para um valor alvo.
    Retorna o valor interpolado.
    """
    n = len(t)
    
    # Encontrar o intervalo [t[i], t[i+1]] que contém o valor_alvo
    for i in range(n - 1):
        if t[i] <= valor_alvo <= t[i+1]:
            # Fórmula da reta: S(t) = y_i + m * (t - t_i)
            # onde m é a inclinação da reta no intervalo
            inclinacao = (y[i+1] - y[i]) / (t[i+1] - t[i])
            resultado = y[i] + inclinacao * (valor_alvo - t[i])
            return resultado
            
    return None


def spline_cubica_natural(t, y, valor_alvo):
    """
    Calcula a Spline Cúbica Natural resolvendo um sistema tridiagonal.
    Retorna o valor interpolado.
    """
    n = len(t) - 1
    
    # Distância entre os pontos
    h = [t[i+1] - t[i] for i in range(n)]
    
    # O coeficiente 'a' da spline é o próprio valor de 'y'
    a = y[:]
    
    # Passo 1: Construção do vetor do lado direito do sistema (alpha)
    alpha = [0.0] * (n + 1)
    for i in range(1, n):
        termo1 = (3.0 / h[i]) * (a[i+1] - a[i])
        termo2 = (3.0 / h[i-1]) * (a[i] - a[i-1])
        alpha[i] = termo1 - termo2
        
    # Passo 2: Resolução do sistema tridiagonal (Algoritmo de Thomas)
    # Inicializando vetores auxiliares
    l = [1.0] * (n + 1)
    mu = [0.0] * (n + 1)
    z = [0.0] * (n + 1)
    
    for i in range(1, n):
        l[i] = 2.0 * (t[i+1] - t[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]
        
    # Condições de contorno da Spline Natural (derivada segunda zero nas pontas)
    l[n] = 1.0
    z[n] = 0.0
    c = [0.0] * (n + 1)
    
    b = [0.0] * n
    d = [0.0] * n
    
    # Substituição reversa para encontrar os coeficientes c, b e d
    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (a[j+1] - a[j]) / h[j] - h[j] * (c[j+1] + 2.0 * c[j]) / 3.0
        d[j] = (c[j+1] - c[j]) / (3.0 * h[j])
        
    # Passo 3: Avaliar o polinômio no intervalo apropriado
    for i in range(n):
        if t[i] <= valor_alvo <= t[i+1]:
            delta_t = valor_alvo - t[i]
            # S(x) = a + b(x-xi) + c(x-xi)^2 + d(x-xi)^3
            resultado = a[i] + b[i] * delta_t + c[i] * (delta_t ** 2) + d[i] * (delta_t ** 3)
            return resultado
            
    return None


# --- BLOCO DE EXECUÇÃO EXIGIDO PELO PROFESSOR ---
if __name__ == "__main__":
    # Dados extraídos do slide 8 (Trajetória do Braço Robótico)
    # t (tempo em segundos): [0.0, 1.0, 2.0, 3.0]
    # y (posição em cm): [2.5, 4.5, 3.0, 6.0]
    tempos = [0.0, 1.0, 2.0, 3.0]
    posicoes =
