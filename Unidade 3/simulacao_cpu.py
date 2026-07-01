import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# 1. PARÂMETROS DO PROBLEMA REAL (PVI)
# -----------------------------------------------------------------------------
T0 = 90.0          # Temperatura inicial da CPU (°C)
T_amb = 25.0       # Temperatura ambiente (°C)
k = 0.01           # Constante de resfriamento do cooler (s^-1)
tol = 0.1          # Tolerância de proximidade térmica (€) para o critério de parada
h = 10.0           # Passo de tempo (em segundos) - mude para testar a estabilidade!

# Função que representa a EDO: dT/dt = f(t, T)
def f(t, T):
    return -k * (T - T_amb)

# Solução analítica exata da EDO para fins de comparação
def solucao_exata(t):
    return T_amb + (T0 - T_amb) * np.exp(-k * t)

# -----------------------------------------------------------------------------
# 2. IMPLEMENTAÇÃO DO MÉTODO DE EULER (DO ZERO)
# -----------------------------------------------------------------------------
t_euler = [0.0]
T_euler = [T0]

t_atual = 0.0
T_atual = T0

# Executa o loop até que a temperatura chegue bem próxima da ambiente (dentro da tolerância)
while abs(T_atual - T_amb) > tol:
    # Fórmula de Euler: T_(n+1) = T_n + h * f(t_n, T_n)
    T_proximo = T_atual + h * f(t_atual, T_atual)
    t_proximo = t_atual + h
    
    T_euler.append(T_proximo)
    t_euler.append(t_proximo)
    
    T_atual = T_proximo
    t_atual = t_proximo

print(f"--- Método de Euler ---")
print(f"Tempo total de resfriamento estimado: {t_atual:.2f} segundos (~{t_atual/60:.2f} minutos)")
print(f"Iterações realizadas: {len(t_euler) - 1}\n")

# -----------------------------------------------------------------------------
# 3. IMPLEMENTAÇÃO DO MÉTODO DE RUNGE-KUTTA DE 4ª ORDEM - RK4 (DO ZERO)
# -----------------------------------------------------------------------------
t_rk4 = [0.0]
T_rk4 = [T0]

t_atual = 0.0
T_atual = T0

while abs(T_atual - T_amb) > tol:
    # Cálculo das 4 inclinações do RK4
    k1 = f(t_atual, T_atual)
    k2 = f(t_atual + h/2.0, T_atual + (h/2.0) * k1)
    k3 = f(t_atual + h/2.0, T_atual + (h/2.0) * k2)
    k4 = f(t_atual + h, T_atual + h * k3)
    
    # Atualização pela média ponderada
    T_proximo = T_atual + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
    t_proximo = t_atual + h
    
    T_rk4.append(T_proximo)
    t_rk4.append(t_proximo)
    
    T_atual = T_proximo
    t_atual = t_proximo

print(f"--- Método Runge-Kutta 4 (RK4) ---")
print(f"Tempo total de resfriamento estimado: {t_atual:.2f} segundos (~{t_atual/60:.2f} minutos)")
print(f"Iterações realizadas: {len(t_rk4) - 1}\n")

# -----------------------------------------------------------------------------
# 4. GERAÇÃO DA SOLUÇÃO ANALÍTICA EXATA PARA O GRÁFICO
# -----------------------------------------------------------------------------
# Cria um vetor de tempo linear cobrindo o mesmo intervalo do RK4 para plotar a curva real
t_max = max(max(t_euler), max(t_rk4))
t_exato = np.linspace(0, t_max, 1000)
T_exato = solucao_exata(t_exato)

# -----------------------------------------------------------------------------
# 5. PLOTAGEM E CUSTOMIZAÇÃO DO GRÁFICO COMPARATIVO
# -----------------------------------------------------------------------------
plt.figure(figsize=(10, 6))

# Sobreposição das 3 curvas conforme exigido no PDF do projeto
plt.plot(t_exato, T_exato, label='Solução Analítica Exata', color='black', linestyle='--', linewidth=2)
plt.plot(t_euler, T_euler, label=f'Método de Euler (h={h}s)', color='red', alpha=0.7, marker='o', markersize=4)
plt.plot(t_rk4, T_rk4, label=f'Método RK4 (h={h}s)', color='blue', alpha=0.8, marker='x', markersize=4)

# Configurações de eixos e legendas acadêmicas
plt.title('Dinâmica de Resfriamento da CPU: Comparação de Métodos Numéricos', fontsize=14, fontweight='bold')
plt.xlabel('Tempo (segundos)', fontsize=12)
plt.ylabel('Temperatura da CPU (°C)', fontsize=12)
plt.axhline(y=T_amb, color='gray', linestyle=':', label=f'Temperatura Ambiente ({T_amb}°C)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)

# Salva a imagem automaticamente no mesmo diretório para vocês colocarem no Overleaf
plt.savefig('grafico_cpu.png', dpi=300, bbox_inches='tight')
plt.show()
