def ajuste_linear_mmq(x, y):
    """
    Calcula os coeficientes 'a' e 'b' da reta P1(x) = ax + b
    usando o Método dos Mínimos Quadrados (MMQ).
    """
    n = len(x)
    
    # Validação básica
    if n != len(y) or n == 0:
        return None
        
    # Inicializando os somatórios
    soma_x = 0.0
    soma_y = 0.0
    soma_xy = 0.0
    soma_x2 = 0.0
    
    # Calculando os somatórios iterativamente
    for i in range(n):
        soma_x += x[i]
        soma_y += y[i]
        soma_xy += x[i] * y[i]
        soma_x2 += x[i] ** 2
        
    # Aplicando as fórmulas diretas para 'a' e 'b' derivadas do sistema normal
    # a = (n * Σxy - Σx * Σy) / (n * Σx² - (Σx)²)
    numerador_a = (n * soma_xy) - (soma_x * soma_y)
    denominador = (n * soma_x2) - (soma_x ** 2)
    
    if denominador == 0:
        raise ValueError("O denominador é zero, impossível ajustar uma reta (pontos sobrepostos ou verticais).")
        
    a = numerador_a / denominador
    
    # b = (Σy - a * Σx) / n  (ou seja, a média de y menos 'a' vezes a média de x)
    b = (soma_y - a * soma_x) / n
    
    return a, b

def prever_valor(a, b, x_alvo):
    """
    Calcula o valor previsto usando a equação da reta encontrada.
    """
    return (a * x_alvo) + b


# --- Execução Principal com os dados da questão ---

# Dados extraídos do material (hora do dia e acessos em milhares)
x_horas = [8.0, 9.0, 10.0, 11.0, 12.0]
y_acessos = [2.1, 2.8, 3.1, 4.0, 4.8]

# 1. Encontrar a equação da reta
a, b = ajuste_linear_mmq(x_horas, y_acessos)

# 2. Prever o tráfego às 13h
hora_previsao = 13.0
acessos_previstos = prever_valor(a, b, hora_previsao)

# Exibição dos resultados formatados
print("--- Ajuste de Curvas (MMQ) ---")
print(f"Coeficiente angular (a): {a:.4f}")
print(f"Coeficiente linear (b):  {b:.4f}")
print(f"Equação da reta:         P1(x) = {a:.2f}x {b:+.2f}")
print("-" * 30)
print(f"Previsão de tráfego às {hora_previsao}h: {acessos_previstos:.4f} (em milhares de acessos)")
