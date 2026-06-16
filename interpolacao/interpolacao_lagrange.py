# Interpolação de Lagrange

def interpolacao_lagrange(x_pontos, y_pontos, x_alvo):
    n = len(x_pontos)
    resultado = 0.0
    for i in range(n):
        termo = y_pontos[i]
        for j in range(n):
            if i != j:
                termo *= (x_alvo - x_pontos[j]) / (x_pontos[i] - x_pontos[j])
        resultado += termo
    return resultado


# --- BLOCO DE EXECUÇÃO EXIGIDO PELO PROFESSOR ---
if __name__ == "__main__":
    # Dados extraídos do slide 6 (Sistema de telemetria do drone autônomo)
    # t (tempo em segundos - eixo x): [1.0, 2.0, 3.0, 4.0, 5.0]
    # y (altitude em metros - eixo y): [1.2, 1.9, 3.2, 5.5, 8.2]
    t_dados = [1.0, 2.0, 3.0, 4.0, 5.0]
    y_dados = [1.2, 1.9, 3.2, 5.5, 8.2]
    t_alvo = 3.5

    # Execução do algoritmo nativo
    altitude_estimada = interpolacao_lagrange(t_dados, y_dados, t_alvo)

    # --- RETORNO DA RESPOSTA DO ALGORITMO ---
    print("=" * 50)
    print("        RESULTADO DA INTERPOLAÇÃO DE LAGRANGE       ")
    print("=" * 50)
    print(f"Dados de Tempo (t):    {t_dados} s")
    print(f"Dados de Altitude (y): {y_dados} m")
    print("-" * 50)
    print(f"Altitude estimada no instante t={t_alvo}s: {altitude_estimada:.4f} metros")
    print("=" * 50)
