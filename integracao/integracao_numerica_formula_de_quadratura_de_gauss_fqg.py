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
        raise ValueError("O algoritmo suporta apenas n=2 ou n=3.")

    integral = 0.0
    
    # Cálculo do Jacobiano para mudança de limites de integração [a, b] para [-1, 1]
    jacobiano = (b - a) / 2.0
    media_ab = (b + a) / 2.0

    # Laço de repetição (regra do projeto) para somatório
    for i in range(n_pontos):
        # Mapeando o ponto t_i para o intervalo [a, b]
        x_i = jacobiano * t[i] + media_ab
        
        # Somatório: peso * função(x_i) * jacobiano
        integral += w[i] * funcao(x_i) * jacobiano
        
    return integral


# --- BLOCO DE EXECUÇÃO EXIGIDO PELO PROFESSOR ---
if __name__ == "__main__":
    # Dados extraídos do slide 12 (Torque do motor)
    def funcao_torque(x):
        return 5 * (x ** 3) + (x ** 2) - 12 * x + 4

    limite_inferior = -1.0
    limite_superior = 1.0
    pontos_n = 2

    # Calculando o trabalho total (integral)
    trabalho_total = quadratura_gauss(funcao_torque, limite_inferior, limite_superior, pontos_n)

    # Exibindo o retorno do algoritmo
    print("--- Resultado da Quadratura de Gauss ---")
    print(f"Função integrada:      f(x) = 5x³ + x² - 12x + 4")
    print(f"Limites de integração: [{limite_inferior}, {limite_superior}]")
    print(f"Número de pontos (n):  {pontos_n}")
    print("-" * 40)
    print(f"Trabalho total (Integral calculada): {trabalho_total:.4f}")
