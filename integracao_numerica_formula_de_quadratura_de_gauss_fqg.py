def quadratura_gauss(funcao, a, b, n_pontos):
    """
    Calcula a integral de uma função usando a Quadratura de Gauss.
    Pontos e pesos fixados para n=2 e n=3 no intervalo [-1, 1].
    """
    # Definição dos pontos (t) e pesos (w)
    if n_pontos == 2:
        # Para n=2, as raízes são +- 1/raiz(3) e os pesos são 1
        raiz_3 = 3 ** 0.5
        t = [-1.0 / raiz_3, 1.0 / raiz_3]
        w = [1.0, 1.0]
    elif n_pontos == 3:
        # Para n=3, as raízes são 0 e +- raiz(3/5)
        raiz_35 = (3.0 / 5.0) ** 0.5
        t = [-raiz_35, 0.0, raiz_35]
        # Pesos correspondentes
        w = [5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0]
    else:
        return "Erro: O algoritmo suporta apenas n=2 ou n=3."

    integral = 0.0
    
    # Cálculo do Jacobiano para mudança de limites de integração [a, b] para [-1, 1]
    # Mesmo o problema pedindo [-1, 1], essa generalização garante que a função funcione para qualquer intervalo
    jacobiano = (b - a) / 2.0
    media_ab = (b + a) / 2.0

    # Laço de repetição (regra do projeto) para somatório
    for i in range(n_pontos):
        # Mapeando o ponto t_i para o intervalo [a, b]
        x_i = jacobiano * t[i] + media_ab
        
        # Somatório: peso * função(x_i) * jacobiano
        integral += w[i] * funcao(x_i) * jacobiano
        
    return integral


# --- Resolução do Problema Específico (Página 12) ---

# 1. Definindo a função da curva de torque do motor
def funcao_torque(x):
    return 5 * (x ** 3) + (x ** 2) - 12 * x + 4

# 2. Definindo os parâmetros exigidos no enunciado
limite_inferior = -1.0
limite_superior = 1.0
pontos_n = 2

# 3. Calculando o trabalho total (integral)
trabalho_total = quadratura_gauss(funcao_torque, limite_inferior, limite_superior, pontos_n)

# 4. Exibindo o retorno do algoritmo
print(f"--- Resultado da Quadratura de Gauss ---")
print(f"Limites de integração: [{limite_inferior}, {limite_superior}]")
print(f"Número de pontos (n): {pontos_n}")
print(f"Trabalho total (Integral calculada): {trabalho_total:.4f}")
