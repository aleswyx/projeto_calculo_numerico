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

