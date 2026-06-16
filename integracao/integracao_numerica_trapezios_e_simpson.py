def regra_dos_trapezios(v, h):
    """
    Calcula a integral numérica pela Regra dos Trapézios Repetida.
    Usa apenas lógica nativa e laços de repetição.
    """
    n = len(v)
    soma = v[0] + v[-1]  # Primeiro e último ponto (peso 1)
    
    # Pontos intermediários (peso 2)
    for i in range(1, n - 1):
        soma += 2 * v[i]
        
    return (h / 2) * soma


def regra_simpson_13(v, h):
    """
    Calcula a integral numérica pela Regra de 1/3 de Simpson Repetida.
    Requer uma quantidade ímpar de pontos.
    """
    n = len(v)
    if n % 2 == 0:
        raise ValueError("A Regra de 1/3 de Simpson requer um número ímpar de pontos.")
        
    soma = v[0] + v[-1]  # Primeiro e último ponto (peso 1)
    
    # Pontos intermediários: alternância de pesos (4 para ímpares, 2 para pares)
    for i in range(1, n - 1):
        if i % 2 != 0:
            soma += 4 * v[i]  # Índices ímpares (peso 4)
        else:
            soma += 2 * v[i]  # Índices pares (peso 2)
            
    return (h / 3) * soma


# --- BLOCO DE EXECUÇÃO EXIGIDO PELO PROFESSOR ---
if __name__ == "__main__":
    # Dados extraídos do material (Página 11 - Carro Elétrico)
    # t (tempo em horas): [0.0, 0.5, 1.0, 1.5, 2.0]
    # v (velocidade em km/h): [0, 40, 65, 80, 90]
    # Como os intervalos são fixos de 30 em 30 minutos: h = 0.5
    tempo = [0.0, 0.5, 1.0, 1.5, 2.0] [cite: 69]
    velocidade = [0, 40, 65, 80, 90] [cite: 69]
    h_constante = 0.5

    # Execução dos métodos nativos
    distancia_trapezio = regra_dos_trapezios(velocidade, h_constante)
    distancia_simpson = regra_simpson_13(velocidade, h_constante)

    # --- RETORNO DA RESPOSTA DO ALGORITMO ---
    print("=" * 50)
    print("   RESULTADO DA INTEGRAÇÃO NUMÉRICA (PÁGINA 11)   ")
    print("=" * 50)
    print(f"Dados de Tempo (t):     {tempo} h")
    print(f"Velocidade (v):         {velocidade} km/h")
    print(f"Passo constante (h):    {h_constante}")
    print("-" * 50)
    print(f"Distância (Regra dos Trapézios): {distancia_trapezio:.2f} km")
    print(f"Distância (Regra 1/3 de Simpson): {distancia_simpson:.2f} km")
    print("=" * 50)
