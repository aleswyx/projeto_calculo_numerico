# Unidade 3: Modelagem e Simulação da Dinâmica Térmica de uma CPU

Este diretório contém o desenvolvimento computacional referente à **3ª Avaliação** da disciplina de Cálculo Numérico. O objetivo deste projeto é modelar o fenômeno físico do resfriamento de uma CPU utilizando Equações Diferenciais Ordinárias (EDOs) e comparar a eficiência e precisão de diferentes métodos de discretização numérica com a solução analítica exata.

---

## 📌 O Problema Físico (PVI)

A dinâmica de resfriamento do processador sob a ação de um cooler é modelada a partir da **Lei de Resfriamento de Newton**, que estabelece que a taxa de variação da temperatura de um corpo é proporcional à diferença entre a sua própria temperatura ($T$) e a temperatura do meio ambiente ($T_{amb}$).

O Problema de Valor Inicial (PVI) é formulado como:

$$\frac{dT}{dt} = -k(T - T_{amb})$$

Com as seguintes condições de contorno e parâmetros reais adotados na simulação:
* **Temperatura Inicial da CPU ($T_0$):** $90.0^\circ\text{C}$ (carga máxima de processamento).
* **Temperatura Ambiente ($T_{amb}$):** $25.0^\circ\text{C}$ (temperatura de referência estável).
* **Constante de Resfriamento ($k$):** $0.01 \text{ s}^{-1}$ (parâmetro de eficiência do sistema de dissipação).
* **Passo de Tempo ($h$):** $10.0 \text{ segundos}$ (intervalo de discretização temporal).
* **Critério de Parada (Tolerância):** $\epsilon = 0.1^\circ\text{C}$ de proximidade com o equilíbrio térmico.

---

## 💻 Métodos Numéricos Implementados

Para garantir a autonomia e cumprir as diretrizes do projeto, as rotinas numéricas foram desenvolvidas **do zero em Python puro** (utilizando apenas laços iterativos `while`), sem o uso de bibliotecas de integração prontas (como `scipy.integrate`).

1. **Método de Euler (1ª Ordem):** Algoritmo de passo simples que aproxima a curva por meio de segmentos lineares baseados na derivada do ponto inicial. Apresenta erro de truncamento global de ordem $\mathcal{O}(h)$.
2. **Método de Runge-Kutta de 4ª Ordem - RK4:** Algoritmo de alta precisão que calcula quatro inclinações distintas dentro de cada intervalo de tempo, aplicando uma média ponderada (regra de Simpson) para mitigar erros locais. Apresenta erro de truncamento global de ordem $\mathcal{O}(h^4)$.
3. **Solução Analítica Exata:** Obtida via integração direta da EDO de variáveis separáveis, servindo como a curva de calibração e gabarito real do sistema:
   $$T(t) = T_{amb} + (T_0 - T_{amb}) \cdot e^{-kt}$$

---

## 📊 Resultados Obtidos

A simulação demonstrou que o sistema leva aproximadamente **650 segundos (~10.8 minutos)** para dissipar o calor e atingir o equilíbrio térmico estável de $25^\circ\text{C}$. 

O script gera automaticamente um gráfico comparativo (`grafico_cpu.png`) que evidencia:
* A sobreposição perfeita e indistinguível entre a curva do método **RK4** e a **Solução Analítica**, validando sua alta fidelidade para o passo $h = 10.0$ s.
* O ligeiro desvio acumulado pelo **Método de Euler** na fase de decaimento mais íngreme, ilustrando didaticamente o impacto do erro de truncamento linear.

---

## 🚀 Como Executar o Script

### Pré-requisitos
Certifique-se de ter o Python 3 e as bibliotecas de visualização instaladas no seu ambiente:
```bash
pip install numpy matplotlib

python simulacao_cpu.py

---
## 👥 Integrantes do Grupo
* Alessandro Franca Ramos
* Eduardo Di Minda Pereira Machado Chagas Oliveira
